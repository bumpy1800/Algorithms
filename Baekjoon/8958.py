# 8958번 문제 : OX퀴즈
# OXXOOOX이런식으로 OX가 주어지고 O일때 점수를 누적하는데 연속하는 O일수록 점수가 더 커진다

num=int(input())

for i in range(num):
    test=input()
    score=0 # 점수와 점수누적하는 변수를 초기화해준다
    count=0
    for j in test: # 문자1개씩 비교해서 연산한다
        if(j=="O"):
            count+=1 # count에 점점 증가시켜준다
            score+=count
        elif(j=="X"): # X면 누적점수 초기화
            count=0
    print(score)