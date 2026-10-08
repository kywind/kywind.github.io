#!/usr/bin/env python3
"""Assemble the static homepage and Hugo blog into the ignored _site directory."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--drafts", action="store_true", help="Include draft blog posts")
args = parser.parse_args()
hugo = shutil.which(os.environ.get("HUGO", "hugo"))
if not hugo:
    parser.exit(1, "Hugo not found. Install Hugo 0.167.0 or set HUGO to its executable path.\n")

# Honor Git's ignore rules and preserve existing public files at their original URLs.
# Include new, uncommitted assets for local previews, without publishing source/config.
files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=str(ROOT)
).decode().split("\0")
if OUT.exists():
    shutil.rmtree(str(OUT))
OUT.mkdir()
for name in sorted(set(files)):
    if not name:
        continue
    rel = Path(name)
    if any(part.startswith((".", "_")) for part in rel.parts):
        continue
    if rel.parts[0] in {"blog", "scripts"} or rel.suffix.lower() in {".md", ".markdown"}:
        continue
    src = ROOT / rel
    if not src.is_file() or src.is_symlink():
        continue
    dst = OUT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(src), str(dst))
cmd = [hugo, "--source", str(ROOT / "blog"), "--destination", str(OUT / "blog"),
       "--gc", "--minify", "--panicOnWarning"]
if args.drafts:
    cmd.append("--buildDrafts")
subprocess.run(cmd, check=True)
(OUT / ".nojekyll").touch()
print("Built " + str(OUT))
