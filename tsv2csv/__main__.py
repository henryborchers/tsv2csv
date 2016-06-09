#!/usr/bin/env python3
import argparse
import os
import sys
from tsv2csv import tsv2csv

def ask_overwrite(statement):

    while True:
        answer = input("{} do you wish to overwrite this? (y/n): ".format(statement))
        if answer.lower() == "y" or answer.lower() == "yes":
            return True
        if answer.lower() == "n" or answer.lower() == "no":
            return False
        print("Invalid response", file=sys.stderr)


def valid_args(args):
    error_msg = []
    warning_msg = []
    if not os.path.exists(args.source):
        error_msg.append("Unable to location {}.".format(args.source))

    extension = os.path.splitext(args.source)[1]
    if extension == ".txt":
        warning_msg.append("{} has an extension of .txt. Treating it as .tsv.".format(args.source))
    if extension not in [".txt", ".tsv"]:
        error_msg.append("{} has an invalid extension.".format(args.source))

    if args.destination is not None:
        path, filename = os.path.split(os.path.abspath(args.destination))
        if not os.path.exists(path):
            error_msg.append("The destination path, {} does not exist.".format(path))
        if not filename.endswith(".csv"):
            error_msg.append("{} does not have a .csv extension.".format(filename))
        # print(path, filename)

    return error_msg, warning_msg
    pass

def main(*args, **kwargs):
    parser = argparse.ArgumentParser(description="Convert a TSV file to a CSV file")
    parser.add_argument("source", help="source tsv file to be converted into a csv file")
    parser.add_argument("--destination", dest="destination", help="name for a csv file")
    args = parser.parse_args()
    errors, warnings = valid_args(args)

    if args.destination is None:
        csv_dest = os.path.abspath(os.path.join(".", os.path.splitext(os.path.basename(args.source))[0] + ".csv"))
    else:
        csv_dest = os.path.abspath(args.destination)

    if len(errors) == 0:
        for warning in warnings:
            print("Warning: {}".format(warning), file=sys.stderr, flush=True)

        if os.path.exists(csv_dest):
            if not ask_overwrite("{} already exists".format(csv_dest)):
                print("Okay. Stopping.")
                exit(0)
        # main(source=args.source, save_as=csv_dest)

    else:
        for error in errors:
            print("Error: {}".format(error), file=sys.stderr)
        exit(1)

    source = os.path.abspath(args.source)
    destination = os.path.abspath(csv_dest)

    print()
    print("Converting {} to {}\n".format(os.path.basename(source), os.path.basename(destination)))
    tsv2csv(source, destination)
    print("Done")

    pass

if __name__ == '__main__':
    main()
