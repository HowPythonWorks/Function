def func1(*langs):
    print(langs, type(langs))
    print("The oldest language is " + langs[1])


def func2(*langs):
    for i in range(len(langs)):
        print("The best language is " + langs[i])


func1("C++", "JS", "Python")
func2("C++", "JS", "Python")


################################################################


# langs = ["C++", "JS", "Python"]

# def func3(langs):
#     for i in range(len(langs)):
#         print("The best language is " + langs[i])

# func3(langs)

################################################################


# func1(langs)
# func2(langs)


# name = ['Bob', 'Marley']


# def func4(f_name, l_name):
#     print(f'Hello, {f_name} {l_name}')


# func4(*name)

################################################################
