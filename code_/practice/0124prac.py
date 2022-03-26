def count_vowels(arg):
    result = 0
    for idx in 'aeiou':
        result += arg.count(idx)
    return result

#print(count_vowels('bbbbhhh'))

def only_square_area(arg1, arg2):
    result = []
    for num in arg1:
        if arg2.count(num) >= 1:
            result.append(num**2)
    return result

#print(only_square_area([32,55,63], [13,32,40,55]))

def get_dict_avg(arg):
    dict_sum = sum(arg.values())
    return dict_sum/len(arg)

my_pts = { 'python' : 80, 'algorithm' : 90, 'django' : 89, 'web' : 83}
#print(get_dict_avg(my_pts))

def count_blood(arg):
    result = {}
    for key in ['A', 'B', 'O', 'AB']:
        result[key] = arg.count(key)
    return result

#print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']))
