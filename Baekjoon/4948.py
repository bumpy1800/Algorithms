# 4948번 문제 : 베르트랑 공준
# 주어진 n에 대해 n~2n사이에 소수를 구하는 문제이다

import math #sqrt()를 사용하기 위함

def sosu(num): # 소수를 수하는 함수
    if num == 1: 
        return False

    for i in range(2, int(math.sqrt(num))+1): # 주어진 수의 제곱근까지만 체크해보면 된다
        if num % i == 0: 
            return False

    return True


li = list(range(2,246912)) # 최대수인 123456의  2배를 미리 리스트의 넣는다

k = []

for i in li: # 246912안에 소수들을 미리 구해놓는다
    if sosu(i):
        k.append(i)

while(1):
    answer = 0
    n = int(input())
    if n == 0: 
        break

    for i in k: # 미리 구해놓는 소수가 주어진 수의 범위안에 몇개가 있는지만 체크
        if ((n < i) and (i <= n*2)):
            answer+=1
    print(answer)