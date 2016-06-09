
import csv
import os

import sys

def tsv2csv(source, destination):
    records = []
    print("Reading rows")
    with open(source, 'r', encoding="utf8") as f:
        reader = csv.DictReader(f, dialect=csv.excel_tab)
        for row in reader:
            records.append(row)
    print("Read {} rows from {}".format(len(records), os.path.basename(source)))

    print("Writing rows")
    with open(destination, "w", encoding="utf8") as f:
        records_written = 0
        fieldnames = list(records[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)
            records_written += 1
        print("Wrote {} rows to {}".format(records_written, os.path.basename(destination)))

    pass
