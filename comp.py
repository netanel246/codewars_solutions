import math


def comp(array1, array2):

    if array1 is None or array2 is None:
        return False

    if (not array1) or (not array2):
        return True

    for b in array2:

        found = False
        for a in array1:
            if is_sqrt(b, a):
                found = True
                break

        if found is False:
            return False

    return True


def is_sqrt(x, y):
    return math.sqrt(x) == y


a1 = [11, 121, 144, 121, 144]
a2 = [11 * 11, 121 * 121, 121 * 121, 144*144, 144*144]

print(comp(a1, a2) is True)
print(comp(True, None) is False)
print(comp([True],[1]))
print(comp([],[1,2,3,4]))
print(comp([None], [0]))
