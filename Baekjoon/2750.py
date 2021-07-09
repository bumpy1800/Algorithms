# 2750번 문제 : 수 정렬하기
# n개의 수가 주어지면 오름차순으로 정렬하기

n=int(input())

num=[]

for i in range(n): # 배열로 저장
    x=int(input())
    num.append(x)

for j in range(n): # 위치바꾸는 알고리즘
    for k in range(j+1,n):
        if(num[j]>num[k]):
            temp=num[j]
            num[j]=num[k]
            num[k]=temp

for p in range(len(num)): # 출력
    print(num[p])