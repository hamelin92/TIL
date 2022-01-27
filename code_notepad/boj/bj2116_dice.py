#인풋 값, 모든 주사위를 모은 이중 리스트 형태 (주사위 단일로는 일반 리스트)로 입력
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
numbers = [1, 2, 3, 4, 5, 6]

# 주사위를 나타낸 리스트와 숫자를 고르면 반대편 숫자를 출력하는 함수
def dice_f(arg, num): 
    if arg.index(num) == 0:
        return arg[5]
    elif arg.index(num) == 5:
        return arg[0]
    elif arg.index(num) == 1:
        return arg[3]
    elif arg.index(num) == 2:
        return arg[4]
    elif arg.index(num) == 3:
        return arg[1]
    else:
        return arg[2]
#각각의 케이스에 대한 최대값들을 모아줄 리스트
local_max_values= []

#맨처음 쌓을 주사위의 밑면 숫자 및 반복문에 필요한 초기값 설정
for num in numbers:
    f_num = num
    local_max = 0
    #d_n 은 대략 주사위에 대한 인덱스
    for d_n in range(N):
        #해당 넘버의 주사위의 밑면과 윗면을 리스트로 저장.
        faces_n = [f_num,  dice_f(dices[d_n], f_num)]
        #만약 위아래에 6,5가 있으면 4, 6은 있고 5가 없으면 5, 6이 없으면 6을 최대값에 더해줌.
        if 6 in faces_n:
            if 5 in faces_n:
                local_max += 4
            else:
                local_max += 5
        else:
            local_max += 6
        #다음 반복순서에 대한 밑면의 숫자 설정.
        f_num = dice_f(dices[d_n], f_num)
    #반복문을 거쳐 계산된 최대값을 리스트에 저장
    local_max_values.append(local_max)
#최대값 후보들이 저장된 리스트에서 최대값 출력
print(max(local_max_values))
#   A
# B C D E
#   F
'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''