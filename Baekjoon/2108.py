# 2108번 문제 : 통계학
# 산술평균, 중앙값, 최빈값, 범위 n개의 수가 주어졌을때 이 네가지 기본 통계값을 구하는 문제
import sys
from collections import Counter

n=int(sys.stdin.readline()) # input()은 시간초과여서 sys를 활용

answer=[]

for i in range(n):
    x=int(sys.stdin.readline()) # 배열에 담는다
    answer.append(x)

answer.sort() # 정렬

bean_s = Counter(answer).most_common() # 최빈값을 구하기위한 Counter활용 빈도수를 튜플형식으로 반환

print(round(sum(answer) / n)) # 평균
print(answer[n // 2]) # 중앙값

if len(bean_s) > 1: # 최빈값이 2개 이상일시 뒤에것과 비교해서 출력
    if bean_s[0][1] == bean_s[1][1]:
        print(bean_s[1][0])
    else:
        print(bean_s[0][0])
else:
    print(bean_s[0][0])

print(answer[-1] - answer[0]) # 범위 인덱스-1은 마지막값