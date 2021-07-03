# 1546번 문제 : 평균
# 점수들이 주어지고 그중 최댓값을 구해서 모든 점수에 점수/최댓값*100으로 고친 후 다시 평균을 구하는 문제

count=int(input())

score=input().split()
score=[int(i) for i in score] # 문자열 리스트를 int형 리스트로 변환

m=max(score) #최댓값을 변수로 따로 저장(max를 이용해 그때그때 구하면 값이 달라짐)

for i in range(count):
    score[i]=score[i]/m*100 # 점수/최댓값*100
    
print(sum(score)/count) # 평균