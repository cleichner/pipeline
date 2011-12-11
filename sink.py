import argparse
import os

from pipeline import pipeline

parser = argparse.ArgumentParser(
    description='Read from the ports and print to stdout.')

parser.add_argument('--in-ports', dest='in_ports', type=int, nargs='*',
                    default=[5555],
                    help='space delimited list of ports to listen on')

args = parser.parse_args()

@pipeline(args.in_ports, None)
def print_out(data):
    print data

