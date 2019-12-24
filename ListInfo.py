from time import strftime

"""
Object for storing list info.
"""

CONST = {
    'time_format': "%Y/%m/%d / %H:%M:%S",
}


class ListInfo:
    def __init__(self, name, note="", time_c="", time_u=""):
        """
        Create list object.
        :param name: name of list
        :param note: note for list
        :param time_c: creation time, false by default when creating new list.
                        Objects can come from file, hence doing it this way.
        :param time_u: update time, false by default when creating new list.
        """
        self.__name = name
        self.__note = note
        self.__entries = []  # Filled later.

        # Existing lists have a creation time, make one for the rest.
        if not time_c:
            self.__time_c = strftime(CONST['time_format'])

        else:
            self.__time_c = time_c

        # Existing lists have a update time, make one for the rest.
        if not time_u:
            self.__time_u = self.__time_c  # Last update is creation time

        else:
            self.__time_u = time_u

    def give_info(self):
        """
        Gives complete contents to the caller.
        :return: dict of list info
        """
        return {
            "name": self.__name,
            "entries": self.__entries,
            "notes": self.__note,
            "time_c": self.__time_c,
            "time_u": self.__time_u
        }

    def add_item(self, item):
        """
        Adds new list entry.
        :param item: list entry object OR another list.
        """
        self.__entries.append(item)
        self.update_time()

    def update_info(self, name, note=""):
        """
        Replaces object's info.
        :param name: new name
        :param note: new note
        """
        self.__name = name
        self.__note = note
        self.update_time()

    def update_time(self):
        """
        Sets the last updated value to be the current date.
        """
        self.__time_u = strftime(CONST['time_format'])
