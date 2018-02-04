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
    # TODO: implement input validation here
    return result


def main():
    list_path = user_prompt("Give path to list file.")


main()