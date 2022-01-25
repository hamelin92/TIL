#a = [4, 1, 2, 10, 8]
#print(f'리스트 a 출력 : {a}')
#print('\n=============================================')
#print(f'sorted(a) : {sorted(a)}')
#print('\n=============================================')
#print(f'sorted 후 리스트 a 출력 : {a}')
#print('\n=============================================')
#print(f'a.sort()를 출력 : {a.sort()}')
#print('\n=============================================')
#print(f'a.sort()를 실행한 후 a를 출력: {a}')

#a = [1, 3, 2]
#b = (4, 7)
#c = 10
#print(f'리스트 a 출력 : {a}')
#print('\n=============================================')
#a.append(b)
#print(f'append(b) 후 리스트 a 출력 : {a}')
#print('\n=============================================')
#a.append(c)
#print(f'append(c) 후 리스트 a 출력 : {a}')
#print('\n=============================================')
#a.extend(b)
#print(f'extend(b) 후 리스트 a 출력 : {a}')
#print('\n=============================================')
#a.extend(c)

#a = [1, 2, 3, 4, 5]
#b = a
#
#a[2] = 5
#
#print(a)
#print(b)
#
#def duplicated_letters(text):
#    result = []
#    b = sorted(text)
#    for letter in list(set(b)):
#        if b.count(letter) > 1:
#            result.append(letter)
#    return result
#
#print(duplicated_letters('apple'))

#def low_and_up(word):
#    result = ''
#    for idx in range(len(word)):
#        if idx%2 == 0:
#            result += word[idx].lower()
#        else:
#            result +=word[idx].upper()
#    return result
#
#print(low_and_up('banana'))

#def lonely(arg):
#    idx = 0
#    while idx < len(arg):
#        if idx < len(arg)-1:
#            if arg[idx] == arg[idx+1]:
#                arg.pop(idx+1)
#            else:
#                idx += 1
#        else:
#            break
#    return arg
#
#print(lonely([1, 1, 3, 3, 0, 1, 1]))
#print(lonely([4,4,4,3,3]))