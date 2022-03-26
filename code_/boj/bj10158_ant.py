w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# t 값이 얼마나 크던간에 x좌표와  y좌표를 각각 봤을때
# 각각 w, h의 2배만큼의 주기를 가지므로 주기로 나눈 나머지 값을 확인한다.
tp = (p+t)%(2*w) # t 시간 후의 x좌표를 구하기 위한 식
tq = (q+t)%(2*h) # t 시간 후의 y좌표
if tp > w: # 한 주기 내에서 w보다 크다는 것은 벽에 한번 반사됐다는 것이다.
    x = 2*w - tp
else: #그렇지 않다면 tp 값 그 자체가 x좌표이다.
    x = tp
if tq > h: # x좌표와 똑같이 y좌표도 계산한다.
    y = 2*h - tq
else:
    y = tq

print(f'{x} {y}')