# 1978번 문제 : 소수 찾기
# 소수란? 1과 자신으로만 나누어지는 수

n = int(input())
num = map(int,input().split())

answer=0

for i in num: # 숫자를 배열로 저장해서 첫줄에 수의 갯수는 사용할 필요가 없다
    count=0
    for j in range(1,i): # 1~i-1까지 해서 딱맞게 떨어지는 수가 1개면 소수이다 여기선 1로만 나누어진 수를 카운트한다
        if(i%j==0):
            count+=1
    if(count==1): # 1개만 카운트 되었다면 소수의 갯수+1
        answer+=1
        
print(answer)