import argparse
import os
import time

from pipeline import pipeline

parser = argparse.ArgumentParser(
    description='Source of numbers to send out over zmq port')

parser.add_argument('--out-port', dest='out_port', type=int, nargs='?',
                    default=int(os.environ.get('OUT_PORT', 5555)),
                    help='the output port that will be pushed to')

parser.add_argument('--delay', dest='delay', type=float, nargs='?',
                    default=float(os.environ.get('DELAY', 0.5)),
                    help='increment value for output stream')

parser.add_argument('--start', dest='start', type=int, nargs='?',
                    default=int(os.environ.get('START', 0)),
                    help='starting value for output stream')

parser.add_argument('--interval', dest='interval', type=int, nargs='?',
                    default=int(os.environ.get('INTERVAL', 1)),
                    help='increment value for output stream')

args = parser.parse_args()

@pipeline(out_port=args.out_port)
def generate_nums():
    time.sleep(args.delay)
    args.start += args.interval
    return str(args.start)

generate_nums.run()
