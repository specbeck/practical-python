# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers if they exist
        if has_headers: headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]

            # Perform type conversions if supplied
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # If no headers append the tuple
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
