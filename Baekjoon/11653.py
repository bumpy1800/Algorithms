# 11653번 문제 : 소인수분해
# 입력된 수를 소인수분해하여 출력하는 문제

n=int(input())

i=2 # 가장 작은 소수는 2이기때문에 1부터 나눌필요없다
while n!=1: # 나누다 보면 끝은 1이되는데 끝이 올때까지 무한루프
    switch=0 # 나누어지는 수가맞는지 판단하는 스위치
    if(n%i==0): # 소수로 나누면 그 뒤로 소수가 아닌수로 나누어질 수 없다\
        n/=i
        switch=1
    else:
        i+=1 # 나누어지지 않는다면 수를 +1

    if(switch==1): # 나누어 진 수만 출력
        print(i)