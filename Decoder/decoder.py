import argparse
import sys


from base import Base
from permutation import Permutation
from morse import Morse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decoder')
    parser.add_argument('--data', help='data to decode')
    decode_list = Base.algorithms + Permutation.algorithms + Morse.algorithms + ["all"]
    parser.add_argument('--decode', help='Specify the decode mode.', default="all", choices=decode_list)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
