"""
Main module
"""
import argparse
from preprocess import tocsv, totals
import settings

def main(arguments):
    print("[START] >> Main-module of BDP <<")
    if arguments.transform:
        tocsv.transformation()
    elif arguments.totals:
        totals.totals()


def parse_arguments():
    parser = argparse.ArgumentParser(
        "BDP - Big data project in the ULiege "
        "'Is the university a good example in electrical consumption?'")

    parser.add_argument("-t", "--transform", type=bool, default=False,
                        nargs='?', const=True, help="Data from .xls to .csv")
    parser.add_argument("-a", "--totals", type=bool, default=False,
                        nargs='?', const=True, help="Generate the totals of "
                                                    "the buildings in one file")
    parser.add_argument("-d", "--difficulty", type=int, default=5, help="")
    arguments, _ = parser.parse_known_args()
    return arguments

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)