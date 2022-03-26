dwarves = [int(input()) for _ in range(9)]
dwarves.sort() # 크기순으로 정렬
diff = sum(dwarves) - 100 # 100에서 초과된 수치
fake = [None, None] # 가짜 난쟁이의 인덱스를 저장
for i in range(8): # 인덱스 0~7 까지 순회
    if dwarves[i] >= diff: # 만약 i번째 난쟁이가 diff값보다 크면 스킵
        continue
    for j in range(i+1, 9): # 인덱스 i~ 8까지 순회
        if dwarves[i] + dwarves[j] == diff: # 만약 i번째 난쟁이와 j번째 난쟁이의 키 합이 diff와 같다면
            fake[0], fake[1] = i, j # 두 인덱스를 fake에 저장하고 순회 종료
            break

for k in range(9): #0~8번까지 fake가 아닌 난쟁이를 출력
    if k not in fake:
        print(dwarves[k])