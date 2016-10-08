# x = 10
#
#
# def foo():
#     x += 1
#     print(x)
# foo()


# odd = lambda x : bool(x % 2)
# numbers = [n for n in range(10)]
# for i in range(len(numbers)):
#     if odd(numbers[i]):
#         del numbers[i]
# odd = lambda x : bool(x % 2)
# numbers = [n for n in range(10)]
# numbers = [n for n in numbers if not odd(n)]
# print(numbers)


def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]
for multiplier in create_multipliers():
    print(multiplier(2))
