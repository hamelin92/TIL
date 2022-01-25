#좌표를 받아 단위정사각형을 왼쪽아래 좌표를 기준으로 모은 집합을 만들어주는 함수입니다.
def r_geo(a,b,c,d):
    result = set()
    for i in range(c-a):
        for j in range(d-b):
            result.add((a+i, b+j))
    return result
rect_union = set()
#r_geo 함수를 통해 만들어진 집합들을 합집합한 결과로 쓰일 공집합을 만들어줍니다.
for num in range(4):#총 4개의 사각형에 대해 시행
    cords = list(map(int,input().split()))#각각의 사각형의 좌표를 받습니다.
    rect_union = rect_union | r_geo(*cords)
#각각의 사각형에 대해 합집합 연산을 통해 rect_union에 r_geo 함수의 결과물을 더해줍니다.
print(len(rect_union))
#최종적으로 rect_union에 len 함수를 사용하여 갯수(사실상 칸수, 넓이와 같음)를 출력합니다.