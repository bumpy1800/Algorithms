# 2577번 문제 : 숫자의 개수
# A,B,C 3개의 자연수가 주어졌을 때 3개를 곱한 수에 0~9가 몇번 쓰였는지 구하는 문제

a=int(input())
b=int(input())
c=int(input())

count=[0 for i in range(10)] # 각 수의 갯수를 카운트하는 리스트 생성

for i in str(a*b*c): # 곱한값을 문자열화 해서 1글자씩 받아온다
    k=int(i) # int로 변환
    count[k]+=1 # 배열 인덱스가 0~9이기때문에 각 자리의 인덱스값에 +1하면 카운팅이 된다

for j in range(len(count)): # 출력
    print(count[j])
