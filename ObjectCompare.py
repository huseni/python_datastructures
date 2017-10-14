
class Restaurant(object):
    bankrupt = False

    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")


x = Restaurant()
y = Restaurant()

print str(x.open_branch())
x.bankrupt = True
print str(y.open_branch())


class SavingsAccount(object):
    """
    This represents saving accounts
    """

    def __init__(self, name, pin, balance= 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __cmp__(self, other):
        return cmp(self._pin, other._pin)

    def __lt__(self, other):
        print "A __lt__ called"
        return self._pin < other._pin

    def __gt__(self, other):
        print "B __gt__ called"
        return self._pin > other._pin

    def __eq__(self, other):
        print "B __eq__ called"
        return self._pin == other._pin

s1 = SavingsAccount('huseni', 95133, 100)
s2 = SavingsAccount('taha', 8374, 732)
if s1 > s2:
    print ("Yes")
if s1 < s2:
    print("No")

if s1 == s2:
    print("equal")

def swap(lst, i, j):
    """
    change the position
    :param lst:
    :param i:
    :param j:
    :return:
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

lst = [2, 4, 6, 8]
print lst
swap(lst, 1,3)
print lst

import cProfile
import re
cProfile.run('swap(lst, 1,3)')


class A(object):
    def __eq__(self, other):
        print "A __eq__ called"
        return self.value == other

class B(object):
    def __eq__(self, other):
        print "B __eq__ called"
        return self.value == other

a = A()
a.value = 3
b = B()
b.value = 3
print a == b
