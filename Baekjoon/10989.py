# 10989번 문제 : 수 정렬하기3
# 10만까지의 수가 주어지고 이를 오름차순으로 정렬하는 문제
# 메모리 제한이있다

import sys # 빠르게 입력을 받기 위해 sys입력을 이용

n = int(input())
chk_list = [0] * 10001 # 최대 1만까지 입력되기 때문에 그만큼의 배열을 생성

for i in range(n): # 입력받은 수의 배열index를 1씩늘리고 중복되는 수가 입력되면 1이상이 될것이다
    m = int(sys.stdin.readline())
    chk_list[m] += 1

for j in range(10001): # 배열 전체를 탐색하면서 1로 활성화되어있는 index를 출력해준다
    if chk_list[j] != 0:
        for k in range(chk_list[j]): # 만약 2라면 2번출력을 해준다
            print(j)