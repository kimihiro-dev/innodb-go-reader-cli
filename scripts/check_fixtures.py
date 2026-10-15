#!/usr/bin/env python3
"""Verify immutable local fixture bytes, optionally against the library source."""
import argparse
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "testdata"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source", type=Path, help="library testdata directory")
args = parser.parse_args()
manifest = json.loads((root / "SOURCE.json").read_text())
for name, expected in manifest["files"].items():
    for folder in [root] + ([args.source] if args.source else []):
        data = (folder / name).read_bytes()
        if len(data) != expected["bytes"] or hashlib.sha256(data).hexdigest() != expected["sha256"]:
            raise SystemExit("Fixture mismatch: " + str(folder / name))
print("Fixtures OK:", len(manifest["files"]))
