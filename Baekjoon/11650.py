# 11650번 문제 : 좌표 정렬하기
# 좌표값이 주어지고 이를 x좌표 오름차순으로 정렬하고 x좌표가 같을 경우 y좌표를 비교해서 정렬한다
import sys

n = int(sys.stdin.readline()) # 최대 10만개까지 테스트 케이스가 주어지기때문에 readline을 활용

xy = []

for i in range(n): # 튜플형 리스트로 저장
    x,y=map(int,sys.stdin.readline().split()) 
    xy.append((x,y))

xy = sorted(xy, key = lambda x: (x[0],x[1])) # sorted()를 활용하고 key값이 복수이기때문에 람다식을 이용함

for j in range(n): # 출력
    print(xy[j][0], xy[j][1])