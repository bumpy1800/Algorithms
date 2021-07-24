# 2751번 문제 : 수 정렬하기2
# 오름차순으로 정렬하는데 수의 범위가 넓어서 버블정렬과 선택정렬로는 할 수 없다

n=int(input())
num=[]

for i in range(n): # 배열로 저장
    x = int(input())
    num.append(x)

num=sorted(num) # 파이썬 내부함수 활용

for i in num:
    print(i)