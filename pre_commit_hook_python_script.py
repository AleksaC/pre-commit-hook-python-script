#!/usr/bin/env python

import argparse

import os
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", required=True)
    parser.add_argument("file_paths", nargs="*")
    args = parser.parse_args(argv)

    res = subprocess.run([os.path.abspath(args.script), *args.file_paths])

    return res.returncode


if __name__ == "__main__":
    raise SystemExit(main())
