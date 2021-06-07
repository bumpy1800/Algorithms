# 1193번 분수찾기 문제
num=int(input())

line=1 
while num>line: # line : 몇번째 라인, num : 입력값이자 그 라인에 가장 큰 숫자
    num=num-line
    line+=1
    print(num,line)
if(line%2==0): # 짝수라인과 홀수라인마다 분자분모가 오름차순인지 내림차순인지 다르다
    x=num
    y=(line-num)+1 # 짝수는 분모가 몇번째 숫자인지
elif(line%2!=0):
    x=(line-num)+1 # 홀수는 분자가 몇번째 숫자인지 나타낸다
    y=num
print(x,y, sep="/")
