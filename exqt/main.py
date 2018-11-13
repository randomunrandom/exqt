import os
import sys


def main(fp=sys.stderr, argv=None):

    if argv is None:
        argv = sys.argv[1:]

    fp.write("exqt is working now\n")  # or print("something", file=fp)

