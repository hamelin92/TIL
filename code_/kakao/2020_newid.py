def solution(new_id):
    # 1단계
    new_str = new_id.lower()
    if new_str == new_id:
        print('1단계 변화 없습니다.')
    else:
        print(f'1단계 "{new_id}" -> "{new_str}"')
    new_id = new_str
    new_str = ''
    # 2단계
    filter_list = {45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 95}
    for i in range(len(new_id)):
        if 97 <= ord(new_id[i]) <= 122 or ord(new_id[i]) in filter_list:
            new_str += new_id[i]
    else:
        if new_str != new_id:
            print(f'2단계 "{new_id}" -> "{new_str}"')
        else:
            print('2단계 변화 없습니다.')
    new_id = new_str
    # 3단계
    while new_str.find('..') != -1:
        new_str = new_str.replace('..', '.')
    if new_str != new_id:
        print(f'3단계 "{new_id}" -> "{new_str}"')
    else:
        print('3단계 변화 없습니다.')
    new_id = new_str
    # 4단계
    while len(new_str) > 0 and new_str[0] == '.':
        new_str = new_str[1:]
    while len(new_str) > 0 and new_str[-1] == '.':
        new_str = new_str[0:len(new_str) - 1]
    if new_str != new_id:
        print(f'4단계 "{new_id}" -> "{new_str}"')
    else:
        print('4단계 변화 없습니다.')
    new_id = new_str
    # 5단계
    if new_str == '':
        new_str = 'a'
    if new_str != new_id:
        print(f'5단계 "{new_id}" -> "{new_str}"')
    else:
        print('5단계 변화 없습니다.')
    new_id = new_str
    # 6단계
    new_str = new_str[:15]
    while len(new_str) > 0 and new_str[-1] == '.':
        new_str = new_str[0:len(new_str) - 1]
    if new_str != new_id:
        print(f'6단계 "{new_id}" -> "{new_str}"')
    else:
        print('6단계 변화 없습니다.')
    new_id = new_str
    # 7단계
    while len(new_str) < 3:
        new_str += new_str[-1]
    if new_str != new_id:
        print(f'7단계 "{new_id}" -> "{new_str}"')
    else:
        print('7단계 변화 없습니다.')
    new_id = new_str

    return new_id