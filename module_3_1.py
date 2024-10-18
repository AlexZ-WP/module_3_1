calls = 0

# def string_info(string):
#
#     n = ()
#     n[0:] = len(string)
#     n[1:] = string.upper()
#     n[2:] = string.lower()
#
#     n = string
#
#     return
#
# print(string_info('Capybara'))

def is_contains(string,list_to_search):
    # string = string.lower()
    # list_to_search = list_to_search.lower()

    for i in string:
        if i == list_to_search:
            print('True')
        else:
            print('False')
            # string.lower()
            # list_to_search.lower()
    return
is_contains('Urban', ['ban', 'BaNaN', 'Urban'])











