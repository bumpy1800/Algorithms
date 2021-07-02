# 10250번 문제 : ACM 호텔
# 호텔방의 크기와 손님 수가 주어지고 같은 손님은 각층의 1호실부터 배정된다

test_case = int(input())

for i in range(test_case):

    h,w,n=map(int,input().split()) # h=층수 w=방호수 갯수 n=손님 수
    room=0
    if(n%h==0): # 꼭대기층일 경우 예외처리
        room=100*h+(n//h)
        print(room)
        continue
    for j in range(n%h): # 사람수%층수만큼 +100를 반복하면 층수를 구할 수 있다
        room+=100
    for k in range((n//h)+1): # 사람수//층수만큼 +1해주면 호수를 구할 수 있다
        room+=1
    print(room)