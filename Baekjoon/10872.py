# 10872번 문제 : 펙토리얼
# 0<=n<=12 의 정수가 주어지고 n의 펙토리얼을 출력하는 문제

n=int(input())

answer=1 # 초기값이 1이여야 0일때나 펙토리얼구할때 곱셈에 문제가없다

for i in range(1,n+1): #1~n까지 범위를 지정해주고 차례차례 곱해준다
    answer*=i

print(answer)