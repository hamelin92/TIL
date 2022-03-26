N = int(input())

for i in range(N):
#    a_info = [0,0,0,0]
#    b_info = [0,0,0,0]
    a, *arga = map(int, input().split()) 
    #a는 정수로 받고 나머지 카드 정보를 리스트로 받는다
    b, *argb = map(int, input().split()) 
    #b에 대해서도 마찬가지
#    for mark in arga:
#        if mark == 4:
#            a_info[0] += 1
#        elif mark == 3:
#            a_info[1] += 1
#        elif mark == 2:
#            a_info[2] += 1
#        else:
#            a_info[3] += 1
#    for mark in argb:
#        if mark == 4:
#            b_info[0] += 1
#        elif mark == 3:
#            b_info[1] += 1
#        elif mark == 2:
#            b_info[2] += 1
#        else:
#            b_info[3] += 1
    if arga.count(4) != argb.count(4):
        # 별의 개수가 다를 경우
        if arga.count(4) > argb.count(4):
            #a쪽이 크면 A 승리 아니면 B 승리
            print('A')
        else:
            print('B')
    elif arga.count(3) != argb.count(3):
        #별의 개수가 다르지 않고 동그라미 개수가 다른 경우
        if arga.count(3) > argb.count(3):
            #위와 같다.
            print('A')
        else:
            print('B')
    elif arga.count(2) != argb.count(2):
        #별,동그라미가 같고 네모가 다른 경우
        if arga.count(2) > argb.count(2):
            print('A')
        else:
            print('B')
    elif arga.count(1) != argb.count(1):
        #별 동그라미, 네모가 같고 세모가 다른 경우
        if arga.count(1) > argb.count(1):
            print('A')
        else:
            print('B')
    else: #그 외의 경우, 즉 , 모두 같은 경우 무승부
        print('D')