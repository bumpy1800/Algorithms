# 9020번 문제 : 골드바흐의 추측
# 골트바흐의 추측은 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다는 것이며, 주어진 수를 어떤 소수로 합하면 나오는지 출력하는 문제

prime_list = [False, False] + [True]*10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    b = a
    while a>0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1