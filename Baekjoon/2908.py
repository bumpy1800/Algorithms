# 2908번 문제 : 상수
# 주어진 3자리 수가 주어지면 그 수를 좌우반전해서 큰수를 출력

a,b = map(list,input().split()) # 리스트로 입력을받는다(.reverse함수를 사용하기 위함)

a.reverse() # 좌우반전시켜서 뒤집는다
b.reverse()

a=''.join(a) # 문자열로 만든다
b=''.join(b)

print(max(a,b)) # 큰수 출력