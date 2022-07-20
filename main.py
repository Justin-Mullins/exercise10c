'''

Exercise 10c

Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the
value should be a list containing all of the values from the arguments.

'''

def combine_dicts(dicts):
    output = {}
    for dict in dicts:
        output = output | dict
    return output

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {4: 'd', 5: 'e', 6: 'f'}
dict3 = {7: 'g', 8: 'h', 9: 'i'}
print(combine_dicts([dict1, dict2, dict3]))
