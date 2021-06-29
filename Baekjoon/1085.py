# 1085번 문제 : 직사각형에서 탈출
# 현재위치와 직사각형의 크기가 주어지고 경계선까지 가는 거리의 최솟값을 구하는문제

x,y,w,h=map(int,input().split()) # 현재 위치(x,y), 직사각형 오른쪽위 꼭짓점(w,h) +왼쪽아래 꼭짓점은 (0.0)

answer=min(x, y, (w-x), (h-y)) # 직사각형의 w는 가로 h는 세로이며 현재 위치를 빼주면 남은 길이를 알수있고 혹은 기존 x,y가 더 작을경우 그 값자체가 최솟값이 된다

print(answer)