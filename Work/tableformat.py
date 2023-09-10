# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """Emit the table headings."""
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of table data."""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML"""

    def headings(self, headers):
        print("<tr>", sep="", end="")
        for h in headers:
            print(f"<th>{h}</th>", sep="", end="")
        print("</tr>", sep="")

    def row(self, rowdata):
        print("<tr>", sep="", end="")
        for r in rowdata:
            print(f"<td>{r}</td>", sep="", end="")
        print("</tr>", sep="")


def create_formatter(name):
    """Creates a formatter given an output name"""
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {name}")
