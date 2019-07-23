#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

def main(argv):
    cpu = CPU()

    cpu.load()
    cpu.run()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))