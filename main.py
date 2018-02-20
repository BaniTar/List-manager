"""
This script is for creating and managing lists. Lists themselves
will be stored in files.
"""


def user_prompt(prompt_text):
    """
    Reads user input and returns it to parent.
    :param prompt_text: text for the prompt
    :return: read value
    """
    result = input(prompt_text)
    return result


def get_file_lines(path):
    """
    Reads the lines of a file into a list and returns it.
    :param path: path to file
    :return: either False or list of lines. False means error in reading.
    """
    # Checking for errors.
    try:
        file = open(path, "r")
        lines = file.readlines()
        file.close()

    except OSError:
        return False

    # Clean lines.
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    return lines


def read_list_file(path):
    """
    Reads a file with list entries in it. Cleans and returns the lines.
    :param path: filepath
    :return: list of the file's lines
    """
    # Read contents.
    lines = get_file_lines(path)

    if lines is False:
        print("Error when trying to access file.")
        return []

    elif "".join(lines) == "":
        print("Error: file is empty")
        return []

    # Successful read.
    else:
        return lines


def test_print(list_lines):
    """
    Checks for list validity and prints the list if valid
    :param list_lines: list of the lines of text to print.
    """
    if not list_lines:  # Faulty file.
        print("Error: faulty file.")
        return

    else:
        line_printer(list_lines)


def line_printer(lines):
    """
    Prints lines of a list line by line.
    :param lines: list of strings
    """
    for line in lines:
        print(line)


def main():
    # Get file path from user.
    list_path = user_prompt("Give path to list file:\n> ")
    # Get list (of entries) from file.
    list_entries = read_list_file(list_path)
    # Test print the list.
    test_print(list_entries)


main()
