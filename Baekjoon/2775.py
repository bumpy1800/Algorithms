# 2775번 문제 : 부녀회장이 될테야

apart=[[0 for i in range(14)] for j in range(15)] # 14*14의 2차원배열

for floor in range(len(apart)): # 층
    for ho in range(len(apart)-1): # 호
        if(floor==0):
            apart[floor][ho]=ho+1 # 0층은 호수의 값만큼 사람이 산다
        else:
            apart[floor][ho]=apart[floor-1][ho]+apart[floor][ho-1] # 각 호수의 층사람들을 구해서 넣어준다


t=int(input())

for i in range(t):
    k=int(input())
    n=int(input())
    if(k==0 or n==0): # 예외처리
        print('1')
        break
    print(apart[k][n-1]) # 층은 0층부터인것에 비해 호는 1호부터여서 index상으로 -1해준다
