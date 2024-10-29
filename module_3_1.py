calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

print(string_info('Capybara'))
print(string_info('Armageddon'))



def is_contains(string,list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if string == i.lower():
        #if (string.lower() == i) or (string == i.lower()):
            print(True)
            break
    else:
        print(False)
    return
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)






    






    
    
    
       

























