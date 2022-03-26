def get_secret_number(arg):
    result = 0
    for i in arg:
        result += ord(i)
    return result

print(get_secret_number('tom'))

def get_strong_word(a, b):
    sum_a = 0
    sum_b = 0
    for i in a:
        sum_a += ord(i)
    for j in b:
        sum_b += ord(j)
    if sum_a >= sum_b:
        return a
    else:
        return b
        
print(get_strong_word('z', 'a')) # => 'z'
print(get_strong_word('tom', 'john')) #=> 'john'
