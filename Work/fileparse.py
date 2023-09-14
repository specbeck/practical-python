# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records
    """

    if not has_headers and select:
        raise RuntimeError("Select argument also requires column headers.")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers if they exist
    if has_headers:
        headers = next(rows)
    else:
        headers = []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:  # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        # Perform type conversions if supplied
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # If no headers append the tuple
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
