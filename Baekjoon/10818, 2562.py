# 10818번 문제 : 최소,최대
# n개의 정수가 주어지고 이중 최솟값과 최댓값을 구하는 문제

n=int(input())

num=list(map(int,input().split()))

print(min(num),max(num))

# 2562번 문제 : 최댓값
# 9개의 자연수가 주어지고 이중 최댓값을 찾고 몇번째 수인지 구하는 문제

answer=[]

for i in range(9):
    num=int(input())
    answer.append(num)

print(max(answer))
print(answer.index(max(answer))+1)