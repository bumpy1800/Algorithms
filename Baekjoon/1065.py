# 양의 정수 x의 각 자리가 등차수열을 이루면 그 수는 한수이다
# 이 문제는 1~1000의 숫자가 제시되었을때 그 사이의 한수를 구하는 문제이다

def han_num(n):
    han=0
    x=[]
    for i in range(100,n+1): # 효율을 위해 100부터 반복문을 돌린다
        for j in str(i): # 숫자를 문자화 시켜 x배열의 넣는다
            x.append(j)
        if(int(x[0])-int(x[1])==int(x[1])-int(x[2])): # 한수인지 체크
            han+=1
        x.clear() # 배열 초기화
    return han+99 # 카운트된 수에 99를 더해서 return한다(이 함수엔 100이상만 들어오고 1~99는 한수이기때문)

num = int(input())
if(num<100): # 1~99는 모두 한수이다
    print(num)
elif(num>=100 and num<=1000): # 그외의 숫자를 함수를 작동시킨다
    print(han_num(num))