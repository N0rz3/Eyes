#!/usr/bin/env python3

__author__ = "N0rz3"

if __name__ == "__main__":
    import os
    os.system('title Eyes')
    import sys
    sys.dont_write_bytecode = True
    import asyncio
    from lib.cli import parser
    asyncio.run(parser())
