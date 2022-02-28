"""Demonstration of reading text files

Plain text files can be used as unstructured
data or for a variety of applications to create
persistent storage for data.
"""


# import statments allow you to use other Python
# moddules from other files (Classes, functions, etc.)
# You can think of these like the #include preprocessor
# directives in C/C++
import os


def parse_log_entry(entry):
    """Parse the apache log file entry
    for the following fields:
    
    "Client IP" - - ["Time of Request"] "Request Line" "Request Code" "Size of data"

    Args:
        entry (str): apache log entry
    Return:
        tuple: collection of the above fields
    """

    # Find will locate the first instance of a string
    # within another string.
    ip_address = entry[:entry.find(" ")]
    date_time = entry[entry.find("[") + 1:entry.find("]")]
    quote_index = entry.find('"') + 1
    
    # Find can be provided a starting to being the search
    request = entry[quote_index:entry.find('"', quote_index)]
    request_code, request_size = entry.split(" ")[-2:]

    return (ip_address, date_time, request, request_code, request_size)


def read_apache_log_file(file_path):
    """Read a apache log file

    Args:
        file_path (str): path to an apache log file
    """

    # with can be used with resources to help with
    # ensuring that closing a stream happens
    # automatically. You can use the "as" statment
    # at the end to give a variable name to the open
    # resource to reference it withint the with
    # block
    # The "r" puts open in read mode. There are other
    # file modes such as "a" for append. You can find
    # a full table of modes here:
    # https://www.tutorialspoint.com/python/python_files_io.htm
    with open(file_path, "r") as apache_log_file:
        for line in apache_log_file:
            # The strip function with no parameters removes
            # leading and trailing whitespace from a string
            print(parse_log_entry(line.strip()))


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
    input_file_path = os.path.join(absolute_path_to_directory, "log_2_small.txt")
    read_apache_log_file(input_file_path)


if __name__ == "__main__":
    main()
