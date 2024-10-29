calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Kate', ['cat', 'BaNaN', 'MoTHer', "KaTE"]))
print(is_contains('cycle', ['recycle', 'cyclic', 'banana']))
print(is_contains('dog', ['faHter', 'broher', 'aPPle']))
print(calls)



