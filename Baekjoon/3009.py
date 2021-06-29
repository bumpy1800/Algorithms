# 3009번 문제 : 네 번째 점
# 세 점이 주어지고 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오
# 1<=좌표<=1000

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

x4=y4=0 # 4번째 점

if(x1==x2): # 직사각형 특성상 x나y중 같은값은 2번이 나오게되고 4번째점은 지금까지 1번만 나온 값이 정답이된다
    x4=x3
elif(x1==x3):
    x4=x2
elif(x2==x3):
    x4=x1
if(y1==y2):
    y4=y3
elif(y1==y3):
    y4=y2
elif(y2==y3):
    y4=y1

print(x4,y4)