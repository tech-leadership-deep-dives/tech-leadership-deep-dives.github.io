#!/usr/bin/env python3
"""Convert YouTube auto-caption VTT to readable paragraph text.

Auto-subs emit rolling captions: every line shows up twice, once as the
"new" line inside a cue that carries inline <NN:NN:NN.NNN><c>word</c> timings
and once as carried-over context in the following cue. We keep only the last
line of cues that carry inline timings -- that is the newly spoken text.
"""
import html
import re
import sys
from pathlib import Path

CUE_TIME = re.compile(r"^(\d\d:\d\d:\d\d\.\d\d\d) --> ")
INLINE_TS = re.compile(r"<\d\d:\d\d:\d\d\.\d\d\d>")
TAG = re.compile(r"</?c[^>]*>")


def cues(text):
    """Yield (start_timestamp, plain_text_of_new_line) for each real cue."""
    for block in text.split("\n\n"):
        lines = [l for l in block.strip().split("\n") if l.strip()]
        if not lines:
            continue
        m = CUE_TIME.match(lines[0])
        if not m:
            continue
        body = lines[1:]
        if not any(INLINE_TS.search(l) for l in body):
            continue  # carried-over duplicate of the previous cue
        new = TAG.sub("", INLINE_TS.sub("", body[-1]))
        new = html.unescape(new).strip()
        if new:
            yield m.group(1), new


def paragraphs(items, max_words=110):
    """Group lines into paragraphs, breaking on speaker turns (>>)."""
    out, buf, start = [], [], None
    for ts, line in items:
        turn = line.startswith(">>")
        if turn:
            line = line[2:].strip()
        long_enough = sum(len(b.split()) for b in buf) >= max_words
        ends_sentence = buf and buf[-1].rstrip().endswith((".", "?", "!"))
        if buf and (turn or (long_enough and ends_sentence)):
            out.append((start, " ".join(buf)))
            buf, start = [], None
        if start is None:
            start = ts
        if line:
            buf.append(line)
    if buf:
        out.append((start, " ".join(buf)))
    return out


def hhmmss(ts):
    h, m, s = ts.split(":")
    s = s.split(".")[0]
    return f"{int(h)}:{m}:{s}" if int(h) else f"{int(m)}:{s}"


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(f"usage: {Path(sys.argv[0]).name} <file.en.vtt> [...]", file=sys.stderr)
        raise SystemExit(2)
    for path in sys.argv[1:]:
        p = Path(path)
        paras = paragraphs(cues(p.read_text(encoding="utf-8")))
        stem = p.name.split(".")[0]
        plain = "\n\n".join(text for _, text in paras)
        timed = "\n\n".join(f"[{hhmmss(ts)}] {text}" for ts, text in paras)
        (p.parent / f"{stem}.txt").write_text(plain + "\n", encoding="utf-8")
        (p.parent / f"{stem}.timed.txt").write_text(timed + "\n", encoding="utf-8")
        print(f"{stem}: {len(paras)} paragraphs, {len(plain.split())} words")


if __name__ == "__main__":
    main()
