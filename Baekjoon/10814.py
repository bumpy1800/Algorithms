# 10814번 문제 : 나이순 정렬
# 나이와 이름을 입력받고 나이순으로 정렬하되 나이가 같으면 먼저 입력받은순으로 정렬한다
import sys

n = int(input())

answer=[]

for i in range(n): # 튜플형식의 리스트에 담는다
    age,name = sys.stdin.readline().split()
    answer.append((int(age),name))

answer = sorted(answer, key= lambda x: x[0]) # 튜플의 첫번째 인자인 나이순으로 정렬하면 sorted()함수로 인해 같아도 입력순으로 정렬

for j in range(n): # 출력
    print(answer[j][0], answer[j][1])