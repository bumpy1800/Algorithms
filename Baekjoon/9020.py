# 9020번 문제 : 골드바흐의 추측
# 골트바흐의 추측은 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다는 것이며, 주어진 수를 어떤 소수로 합하면 나오는지 출력하는 문제

sosu = [False, False] + [True]*10002 # 에라토스테네스의 체를 통해 최대 수이하의 소수들을 구한다

for i in range(2, 10002):
    if sosu[i]:
        for j in range(2*i, 10002, i):
            sosu[j] = False

def sum(m): # 주어진 수의 2분의1 부터 간격을 넓혀 가면서 소수이면서 더했을 시 주어진 수와 같아지는 수를 출력
    x=m//2
    y=x
    while m>0:
        if((sosu[x] and sosu[y]) and (x+y==m)):
            return x,y
        else:
            x-=1
            y+=1


num = int(input())

for i in range(num): # 출력
    n=int(input())
    x,y=sum(n)
    print(x,y)