# 2839번 문제 : 설탕 배달
# 주어진 숫자가 되기까지 3과5를 최소한으로 더하려면 몇번 더해야하는지 구하는 문제
kg = int(input())
answer=0
while 1:
    if(kg%5==0): # 5의 배수면 5만 더하는게 가장 최소인 수가 나온다
        answer+=kg/5
        print(int(answer))
        break
    elif(kg<=0): # 주어진 값이 0이하거나 3을 계속빼도 5의 배수가 안나오면 구할 수 없는 숫자이다
        print('-1')
        break
    kg-=3 # 5의 배수가 나올때 까지 3씩빼고 answer에 1씩 카운트한다
    answer+=1
    