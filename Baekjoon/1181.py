# 1181번 문제 : 단어 정렬
# 알파벳 소문자로 이루어진 n개의 단어가 주어지면
# 길이가 짧은순으로, 길이가 같다면 사전순으로 정렬하는 문제
import sys

n = int(sys.stdin.readline())

answer = []

for i in range(n): # 배열로 문자열을 저장
    answer.append(sys.stdin.readline())

answer=set(answer) # 집합자료형으로 변환해서 중복을 제거
answer=list(answer) # 다시 리스트로 변환

answer = sorted(answer, key= lambda x: (len(x),x)) # 정렬기준이 여러개임으로 sorted()함수와 람다식을 이용해서 길이와 알파뱃순으로 정렬

for j in range(len(answer)): # 출력
    print(answer[j],end='')