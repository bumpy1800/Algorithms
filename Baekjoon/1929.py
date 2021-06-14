# 1929번 문제 : 소수 찾기
# 주어진 두 수 사이의 소수를 모두 출력하는 문제

import math

def sosu(num): # 소수를 구하는 함수
    if (num==1):
        return False
    for j in range(2,int(math.sqrt(num)+1)): # 2*4,4*2 처럼 반대되는건 굳이 필요없는 반복임으로 제곱근까지만 반복
        if(num%j==0):
            return False # 2~j사이에 딱맞게 나누어지는 수가 있다면 소수가 아니다
    return True

n,m=map(int,input().split())

for i in range(n,m+1):
    if(sosu(i)): # 소수함수에서 True받은것만 출력
        print(i)
