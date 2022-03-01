"""Demonstration of reading CSV files

CSV (comma separate values) files are
structured data files that allows for
retrieval of data by indicating each data
field using a specific character (a comma
for CSV values). These can be a common
format for many datasets especially when
the data does not exhibit a hierarchical
structure.

Note that you will need to run this program
from WITHIN this directory or you will be
unable to open the file.

You can find details about the csv module here:
https://docs.python.org/3.9/library/csv.html
"""


# import statments allow you to use other Python
# moddules from other files (Classes, functions, etc.)
# You can think of these like the #include preprocessor
# directives in C/C++
import csv
import os


def grade_distribution_report(input_file_path, output_file_path):
    """Read a comma separated values
    (CSV) file

    Args:
        input_file_path (str): absolute path to a CSV file
        output_file_path (str): absolute path to the outpufile
    """

    grade_distribution = {}

    with open(input_file_path, "r") as csv_file:
        # The csv module's reader object can take an
        # input file in a comma separated format
        csv_data = csv.reader(csv_file)
        
        # I'm using next to skip the csv header
        # (the first row) because I won't use
        # this data
        next(csv_data)

        for line in csv_data:
            if line[-1] in grade_distribution:
                grade_distribution[line[-1]] += 1
            else:
                grade_distribution[line[-1]] = 1
    
    # The "w" puts open in write mode and allows for
    # files to be created. There are other file modes
    # such as "a" for append. You can find a full table
    # of modes here:
    # https://www.tutorialspoint.com/python/python_files_io.htm
    with open(output_file_path, "w") as output_file:
        output_file.write("Grade Distribution\n")
        for key, value in grade_distribution.items():
            output_file.write(f"{key}: {value}\n")


def final_grade_report(input_file_path):
    """Read a comma separated values using the DictReader
    To easily reference data based on the CSV header (the
    first row containing names for all the fields)

    Args:
        input_file_path (str): absolute path to a CSV file
    """

    with open(input_file_path, "r") as csv_file:
        # Using the DictReader, the field name header
        # supplied with some CSV files can be used to
        # reference the data instead of simply using
        # list indices.
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(f"{row['Firstname']} {row['Lastname']}: {row['Grade']}")


def main():
    # If this script in not run within this directory, we will not be
    # able to find grades.csv via a relative path. Python can help us
    # locate a path to the file so it doesn't matter what the current
    # working directory is for our terminal.
    #
    # Locate the absolute path to this script
    absolute_path_to_script = os.path.realpath(__file__)
    # Identify the absolute path to the directory where this script
    # resides
    absolute_path_to_directory = os.path.dirname(absolute_path_to_script)
    # Join the directory path with a filename for the intput using the
    # correct path separators depending on the OS (Win/Unix).
    input_file_path = os.path.join(absolute_path_to_directory, "grades.csv")
    output_file_path = os.path.join(absolute_path_to_directory, "report.txt")
    
    grade_distribution_report(input_file_path, output_file_path)

    final_grade_report(input_file_path)


if __name__ == "__main__":
    main()
