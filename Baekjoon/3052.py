# 3052번 문제 : 나머지
# 주어진 수와 42를 나누고 그 값이 총 몇개인지 구하는 문제이다 중복되는 숫자는 카운팅하지 않는다

count=[]

for i in range(10):
    num = int(input())
    count.append(int(num%42)) # 나눈값을 리스트에 저장

count=set(count) # 집합자료형으로 변환(집합자료형은 중복을 허용하지 않음)
count=list(count) # 중복이 제거된상태에서 다시 리스트형으로 변환

print(len(count)) # 리스트의 길이 즉, 중복되지않은 나머지갯수를 출력