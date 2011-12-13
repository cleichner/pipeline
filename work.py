import argparse
import os

from pipeline import pipeline

parser = argparse.ArgumentParser(
    description='Read from the in_ports and push 2* the read value to the '
                'out_port.')

parser.add_argument('--out-port', dest='out_port', type=int, nargs='?',
                    default=int(os.environ.get('IN_PORT', 5555)),
                    help='the output port that will be pushed to')

parser.add_argument('--in-ports', dest='in_ports', type=int, nargs='*',
                    default=[5556],
                    help='space delimited list of ports to listen on')

args = parser.parse_args()

@pipeline(in_ports=args.in_ports, out_port=args.out_port)
def double_echo(data):
    return 2 * data

double_echo.run()
