import argparse
import os
import sys

from pipeline import pipeline

parser = argparse.ArgumentParser(
    description='read from stdin and send contents to a ZMQ socket.')

parser.add_argument('--out-port', dest='out_port', type=int, nargs='?',
                    default=int(os.environ.get('OUT_PORT', 5558)),
                    help='the port that zc will push over')

args = parser.parse_args()

@pipeline(None, args.out_port)
def read():
    try:
        return raw_input()
    except EOFError:
        sys.exit(0)

