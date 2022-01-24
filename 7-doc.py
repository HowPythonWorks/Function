from datetime import datetime


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter

    Parameters:   
        name(str): Name of user

    Returns:
        None
    """
    print(f'Hello, {name}. How are you?')


# help(greet)
# print(greet.__doc__)
################################################################


# def say_time():
#     '''
#     Print current time
#     :return: None
#     '''
#     print(datetime.now().strftime('%H:%M'))


# say_time()
# 'q' key for exit
# help(say_time)


################################################################


# def get_time():
#     '''
#     Generate time in HH:MM format
#     :return: String
#     '''
#     return datetime.now().strftime('%H:%M')


# get_time()
# help(get_time)
