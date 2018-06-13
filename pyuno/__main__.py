#!/usr/bin/python
# -*- coding: utf-8 -*-

"""argparse entrypoint script"""

import argparse
import sys


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argparser for trivector"""
    parser = argparse.ArgumentParser(
        description=""
    )
    return parser


def main(argv=sys.argv[1:]):
    """argparse function"""
    parser = get_parser()
    args = parser.parse_args(argv)

    return 0


if __name__ == "__main__":
    sys.exit(main())
