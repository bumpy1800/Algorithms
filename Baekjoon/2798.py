# 2798번 문제 : 블랙잭
# 카드의 수와 값이 주어지고 카드중 3장의 합이 주어진 값과 가장 가까운값을 찾아내는 문제

n,m = map(int,input().split()) # n=카드의 수, m=목표값

card = list(map(int,input().split())) # 카드의 값들을 list로 저장

answer=[]
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            answer.append(card[i]+card[j]+card[k])

answer=[i for i in answer if i<=m]
print(max(answer))