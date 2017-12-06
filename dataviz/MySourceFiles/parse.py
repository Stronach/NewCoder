#parse.py
"""
  From the original file.
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""
import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    opened_file = open(raw_file)
    # Open CSV file

    csv_data = csv.reader(opened_file, delimiter=delimiter)
    # Read CSV file

    parsed_data = []
    # Setup empty list

    fields = csv_data.next()
    # Skip over teh first line of the file for the headers

    for row in csv_data:
        parsed_data.append(dict(zip(fields,row)))
    # Iterate over each row of the csv file, zip together field -> value

    opened_file.close()
    # Close CSV file

    return parsed_data
    # Build a data structure to return parsed data.

def main():
    new_data = parse(MY_FILE, ",")
    # Call our parse function and give it the needed parameters
    print(new_data)
    # show's what it looks like.

if __name__ == "__main__":
    main()
