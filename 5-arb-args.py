def func1(**details):
    print(details, type(details))

    for key, value in details.items():
        print("{}: {}".format(key, value))


func1(Name="val_Name", Project="val_Project", Number="val_Number")

# func1(a=1, b=2)


################################################################


# def func2(*members, **features):
#     for member in members:
#         print(member)

#     for key, value in features.items():
#         print("{}: {}".format(key, value))


# func2("Bob", "Marley", Name="val_Name",
#       Project="val_Project", Number="val_Number")
