# 3053번 문제 : 택시 기하학
# 반지름이 주어지고 그 수는 10000보다 작거나 같다 첫째줄엔 원의 넓이를, 둘째줄엔 택시 기하학에서 원의 넓이를 구한다

from math import pi

r=int(input())

print(r*r*pi) # 유클리드 기하학에서의 원의 넓이
print(r*r*2) # 택시 기하학에서의 원의 넓이