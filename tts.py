import asyncio
import hashlib
import json
import os
import re
import sys
import time
import traceback
import unicodedata
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "3")
os.environ.setdefault("OMP_WAIT_POLICY", "PASSIVE")
os.environ.setdefault("MKL_NUM_THREADS", "3")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "3")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "3")

CACHE_DIR = Path(__file__).resolve().parent / "data" / "tts-cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

HAS_ZEROTTS = False
try:
    from zerotts import ZeroTTS as TTS, normalize_vi_text
    from zerotts.chunking import normalize_punctuation
    HAS_ZEROTTS = True
except Exception:
    HAS_ZEROTTS = False

HAS_EDGETTS = False
try:
    import edge_tts
    HAS_EDGETTS = True
except Exception:
    HAS_EDGETTS = False

VIETNAMESE_ALLOWED_RE = re.compile(
    r"[^0-9a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠ-ỹ\s.,!?]"
)
BRACKET_EMOTE_RE = re.compile(r"\[[^\]]{1,24}\]")
REPEATED_CHARS_RE = re.compile(r"(.)\1{2,}", re.IGNORECASE)
MULTI_PUNCT_RE = re.compile(r"([.,!?])\1+")
MULTI_SPACE_RE = re.compile(r"\s+")


def emit(payload: dict) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def clean_and_normalize_text(raw_text: str) -> str:
    if not raw_text:
        return ""
    text = unicodedata.normalize("NFC", unicodedata.normalize("NFKC", str(raw_text)))
    text = BRACKET_EMOTE_RE.sub(" ", text)
    text = VIETNAMESE_ALLOWED_RE.sub(" ", text)
    text = MULTI_PUNCT_RE.sub(r"\1", text)
    text = REPEATED_CHARS_RE.sub(r"\1\1", text)
    text = MULTI_SPACE_RE.sub(" ", text).strip(" .,!?-")
    letters = re.findall(r"[a-zA-ZÀ-ỹĂăĐđĨĩŨũƠơƯư]", text)
    if len(letters) < 2:
        return ""
    if len(text) > 160:
        text = text[:160].rsplit(" ", 1)[0]

    if HAS_ZEROTTS:
        try:
            normalized = normalize_vi_text(text)
            normalized = normalize_punctuation(normalized).strip()
            text = normalized
        except Exception:
            pass

    text = VIETNAMESE_ALLOWED_RE.sub(" ", text)
    text = MULTI_SPACE_RE.sub(" ", text).strip()
    if text and text[-1] not in ".!?":
        text += "."
    return text


def main() -> None:
    t0 = time.time()
    tts = None
    voices = ["maichi"]
    engine_name = "EdgeTTS Neural"

    if HAS_ZEROTTS:
        try:
            tts = TTS.from_pretrained("zeroweight-ai/ZeroTTS", intra_op_num_threads=3)
            voices = tts.list_voices() or ["maichi"]
            engine_name = "ZeroTTS"
        except Exception as e:
            tts = None

    load_sec = round(time.time() - t0, 2)
    emit({
        "type": "ready",
        "model": engine_name,
        "voice": "maichi",
        "voices": voices,
        "sampleRate": 24000,
        "loadSec": load_sec,
    })

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req_id = None
        try:
            req = json.loads(line)
            req_id = req.get("id")
            text = (req.get("text") or "").strip()
            voice = (req.get("voice") or "maichi").strip().lower()

            norm_text = clean_and_normalize_text(text)
            if not norm_text:
                emit({"type": "result", "id": req_id, "ok": False, "error": "Filtered empty/spam text"})
                continue

            cache_key = hashlib.sha1(f"v4::{voice}::{norm_text}".encode("utf-8")).hexdigest()[:20]
            ext = "wav" if (HAS_ZEROTTS and tts is not None) else "mp3"
            out_name = f"{voice}_{cache_key}.{ext}"
            out_path = CACHE_DIR / out_name

            if out_path.is_file() and out_path.stat().st_size > 200:
                emit({
                    "type": "result",
                    "id": req_id,
                    "ok": True,
                    "cached": True,
                    "voice": voice,
                    "file": out_name,
                    "url": f"/tts-cache/{out_name}",
                    "synthSec": 0.0,
                })
                continue

            t_synth = time.time()
            if HAS_ZEROTTS and tts is not None:
                raw_wav = tts.synthesize(norm_text, voice=voice, eoa_extra_frames=2)
                if raw_wav is None or raw_wav.size == 0:
                    emit({"type": "result", "id": req_id, "ok": False, "error": "No audio generated"})
                    continue
                tts.save_audio(raw_wav, str(out_path))
            elif HAS_EDGETTS:
                edge_voice = "vi-VN-HoaiMyNeural"
                asyncio.run(edge_tts.Communicate(norm_text, edge_voice).save(str(out_path)))
            else:
                emit({"type": "result", "id": req_id, "ok": False, "error": "No TTS engine available"})
                continue

            synth_sec = round(time.time() - t_synth, 2)
            emit({
                "type": "result",
                "id": req_id,
                "ok": True,
                "cached": False,
                "voice": voice,
                "file": out_name,
                "url": f"/tts-cache/{out_name}",
                "synthSec": synth_sec,
                "durationSec": 3.0,
            })
        except Exception as exc:
            emit({
                "type": "result",
                "id": req_id,
                "ok": False,
                "error": str(exc),
            })


if __name__ == "__main__":
    main()
