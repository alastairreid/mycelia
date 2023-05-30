#! /usr/bin/env python3

import json
import os
import re
import string
import sys
import yaml

from yaml import dump
from yaml import CDumper as Dumper

def read_yaml(f):
    """Read the YAML frontmatter on a page"""
    with open(f) as file:
        ls = file.readlines()
        t = ls[1:].index("---\n")
        header = ls[1:t+1]
        header = yaml.safe_load("".join(header))
        return header

def name2basename(x):
    x = x.lower()
    x = x.replace(" ", "-")
    return x

def path2basename(f):
    f = os.path.basename(f)
    (f, _) = os.path.splitext(f)
    return f

def do_files(fs):
    headers = { path2basename(f): read_yaml(f) for f in fs }
    titles = { f: h['title'] for f, h in headers.items() }
    refs = {}
    for src, h in headers.items():
        for n in h["notes"]:
            tgt = name2basename(n)
            refs.setdefault(tgt, set()).add(src)
    refs = { tgt: [ [src, titles[src]] for src in sorted(srcs) ] for (tgt, srcs) in refs.items() }
    print(yaml.dump(refs))

def main():
    do_files(sys.argv[1:])

main()
