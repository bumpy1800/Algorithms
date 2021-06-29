# 4153번 문제 : 직각삼각형
# 피타고라스의 정리문제이며 삼각형의 각변의 길이가 주어지고 직각삼각형이면 right를 출력한다 마지막엔 0 0 0이 입력된다

while 1:
    answer = list(map(int,input().split())) # 입력받은 값을 리스트로 저장합니다(정렬 기능을 이용하기 위함)

    if(sum(answer)==0):
        break
    
    answer.sort() # 오름차순으로 정렬하여 가장 큰 값이 맨뒤로 가게한다

    if((answer[0]*answer[0]) + (answer[1]*answer[1])==(answer[2]*answer[2])): # 피타고라스의 정리를 이용하여 직각삼각형 여부를 판단
        print("right")
    else:
        print("wrong")