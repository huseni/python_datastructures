#!/usr/bin/env python


# How to construct the custom array object
class ConstructArray(object):
    """
    This class represents an array
    """

    def __init__(self, capacity, fillval=None):
        """
        Static size of the array
        :param capacity:
        :param fillval:
        """
        self._items = list()
        for count in xrange(capacity):
            self._items.append(fillval)

    def __len__(self):
        """
        size of array list
        :return:
        """
        return len(self._items)

    def __str__(self):
        """
        String representation of object
        :return:
        """
        return str(self._items)

    def __iter__(self):
        """
        Iter the items in the list
        :return:
        """
        return iter(self._items)

    def __getitem__(self, item):
        """
        get the item value
        :param item:
        :return:
        """
        return self._items[item]

    def __setitem__(self, item, value):
        """
        Set the item value
        :param key:
        :param value:
        :return:
        """
        self._items[item] = value


a = ConstructArray(40)

print(len(a))
for i in xrange(len(a)):
    a[i] = i + 1

print("************* Printing the array ************")
for item in a:
    print item
