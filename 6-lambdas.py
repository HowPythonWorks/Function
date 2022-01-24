import math


x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))


################################################################


# def emoji_factory(emoji):
#     return lambda n: n * emoji


# bread_factory = emoji_factory('🍞')
# breads = bread_factory(5)
# print(breads)


################################################################


# def createLog(base):
#     return lambda n: math.ceil(math.log(n, base))


# lg10 = createLog(10)
# lg2 = createLog(2)
# ln = createLog(math.e)

# print('lg10(100)', lg10(100))
# print('lg10(1000)', lg10(1000))

# print('lg2(8)', lg2(8))
# print('lg2(16)', lg2(16))

# print('ln(1)', ln(1))
