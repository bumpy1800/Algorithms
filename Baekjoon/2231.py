# 2231번 문제 : 분해합
# 자연수m의 각자릿수와 자연수m을 더해서 n이 나왔다면 m은 n의 생성자이다
# 주어진 숫자의 생성자중 가장 작은수를 구하는 문제

n=int(input())

for i in range(1,n): # 1부터 n까지 모든 경우의 수를 점검
    m=sum(map(int,str(i))) # 각 자릿수의 합
    answer=i+m # 각 자릿수의 합과 i를 더함
    if(answer==n): # 생성자라면 출력하고 반복문 탈출
        print(i)
        break
else: # break없이 반복문이 종료될시 생성자가 없는것이므로 0출력
    print(0)