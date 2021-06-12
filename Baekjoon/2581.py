# 2581번 문제 : 소수 찾기
# 소수란? 1과 자신으로만 나누어지는 수
# 주어진 2개의 수 사이의 소수를 찾고 그 소수들의 최솟값과 그 합을 찾아내는 문제

n = int(input())
m = int(input())

answer=[]

for i in range(n,m+1): 
    count=0
    if i > 1:   # 1보다 큰 수만 검사를 해야 1~1이라는 입력이 나왔을시 -1이 나온다
        for j in range(2,i): # 2부터 i-1까지 해서 불필요한 검사시간을 줄인다
            if(i%j==0):
                count+=1 # 2~i-1사이에 카운트가 발생하면 그건 소수가 아니다
                break # 이미 소수임이 증명됬으면 불필요한 검사시간을 늘릴필요가 없다
        if(count==0):
            answer.append(i) # answer리스트에 추가한다
if(len(answer)>0): # 리스트의 길이가 0이상이면 값이 있는거다
    print(sum(answer)) # 합출력
    print(min(answer)) # 최소값출력
else:
    print(-1)
