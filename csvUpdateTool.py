"""Python CSV handling demo, simple version."""

import csv
from pathlib import Path


def transform():
    """Filters and transforms each row of input CSV, with output to a separate file."""
    inpath = Path("report.csv")
    outpath = Path("out/transformed.csv")
    outpath.parent.mkdir(exist_ok=True)
    args = {"newline": ""}
    with inpath.open("r", **args) as infile, outpath.open("w", **args) as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, ["Email", "Curriculum (Course)", "Date Completed", "Expiration Date"])
        
         

        writer.writeheader()

        for row in reader:
            new_row = {
                "Email": row["Email"],
                "Curriculum (Course)": row["Curriculum (Course)"],
                "Date Completed": row["Date Completed"],
                "Expiration Date": row["Expiration Date"]        
                }
            writer.writerow(new_row)


if __name__ == "__main__":
    transform()
