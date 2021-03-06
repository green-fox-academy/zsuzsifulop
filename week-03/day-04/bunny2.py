# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).  # nopep8


def number_of_bunnys(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 2 + number_of_bunnys(n - 1)
    elif n % 2 == 1:
        return 3 + number_of_bunnys(n - 1)


print(number_of_bunnys(5))
