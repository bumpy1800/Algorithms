# 1427번 문제 : 소트인사이드
# 수가 주어지면 각 자릿수를 내림차순으로 정렬하는 문제

num = input()

answer=[]

for i in num: # 배열로 저장
    answer.append(i)

answer.sort(reverse=True) # sort를 이용한 정렬
answer=''.join(answer) # [1,2,3,4]를 1234로 붙여줌

print(answer)