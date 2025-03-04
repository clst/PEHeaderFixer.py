#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path
from pprint import pprint
from warnings import warn
from glob import glob
import gc

import pefile

presets = {
	"winxp": {
		"MajorOperatingSystemVersion": 5,
		"MinorOperatingSystemVersion": 1,
		"MajorSubsystemVersion": 5,
		"MinorSubsystemVersion": 1,
	},
	"win2k": {
		"MajorOperatingSystemVersion": 5,
		"MinorOperatingSystemVersion": 0,
		"MajorSubsystemVersion": 5,
		"MinorSubsystemVersion": 0,
	},
	"winnt4": {
		"MajorOperatingSystemVersion": 4,
		"MinorOperatingSystemVersion": 0,
		"MajorSubsystemVersion": 4,
		"MinorSubsystemVersion": 0,
	},
}


def main():
	parser = argparse.ArgumentParser(description="CLI tool to fix EXE files for older Windows")
	parser.add_argument("--json", type=str, default=None, help="A file with JSON string, describing which fields of the header to patch")
	parser.add_argument("--preset", type=str, default=None, help="A hardcoded preset")
	parser.add_argument("file", type=str, nargs="+", help="Path to a file to patch")
	args = parser.parse_args()

	toPatch = {}
	if args.preset is not None:
		for preset in args.preset.split(","):
			toPatch.update(presets[preset])

	if args.json is not None:
		if args.json == "-":
			toPatch = sys.stdin.read()
		else:
			toPatch = Path(args.json).read_text()
		toPatch.update(json.loads(toPatch))

	pprint(toPatch)

	if args.file[0] == "**":
		#patch everything hidden option:
		args.file = []
		args.file.extend(Path('.').glob('**/*.exe'))
		args.file.extend(Path('.').glob('**/*.dll'))
	else:
		for f in args.file[:]:
			args.file.remove(f)
			if '*' in f:
				args.file += glob(f)
			else:
				args.file.append(Path(f))

	print(args)
	for f in args.file:
		print(f)
		p = pefile.PE(f)

		patched = False
		for headerName in ("OPTIONAL_HEADER", "FILE_HEADER", "DOS_HEADER"):
			if hasattr(p, headerName):
				h = getattr(p, headerName)

				for k, v in toPatch.items():
					try:
						oldV = getattr(h, k)
					except AttributeError:
						continue
					else:
						if oldV != v:
							patched = True
							setattr(h, k, v)
							print(f, ":", k, ":", oldV, "->", v)

		if patched:
			tempdata = p.write()
			del p
			gc.collect()
			with open(str(f),'wb+') as fn:
				fn.write(tempdata)


if __name__ == "__main__":
	main()
