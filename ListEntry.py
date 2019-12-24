"""
A normal list entry object that is not a list.
"""

from time import strftime


class ListEntry:
    def __init__(self, name, note="", deadline="", time_c="", time_u=""):
        """
        Initializes necessary variables
        :param name:
        :param note:
        :param deadline:
        :param time_c: creation time, false by default when creating new list.
                    Objects can come from file, hence doing it this way.
        :param time_u: update time, false by default when creating new list.
        """
        # Stub
