# 4344번 문제 : 평균은 넘겠지
# 테스트케이스의 갯수와 학생수&N명의 점수가 주어지고 평균을 소수점 셋째 자리까지 출력한다

num=int(input())

for i in range(num):
    case=list(map(int,input().split())) # 입력받은 값을int형list로 변환한다
    total=sum(case[1:])/case[0] # 평균을 구한다
    count=0
    for j in range(1,len(case)): # 첫번째 index는 학생수이니 1부터 반복문을 돌린다
        if(total<case[j]): # 평균보다 높은 학생을 카운팅한다
            count+=1
    answer=count/case[0]*100 # 평균보다 높은 학생의 비율
    print("{:.3f}%".format(answer)) # format을 이용하여 소수점 셋째 자리까지 출력