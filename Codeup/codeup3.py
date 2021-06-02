#코드업 파이썬 기초문제 61
a,b=input().split()
print(int(a)|int(b))

#코드업 파이썬 기초문제 62
a,b=input().split()
print(int(a)^int(b))

#코드업 파이썬 기초문제 63
a,b=input().split()
a=int(a)
b=int(b)
c=a if a>=b else b
print(c)

#코드업 파이썬 기초문제 64
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=(a if a<=b else b) if (a if a<=b else b) <= c else c
print(d)

#코드업 파이썬 기초문제 65
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if (a % 2) == 0:
    print(a)
if (b % 2) == 0:
    print(b)
if (c % 2) == 0:
    print(c)

#코드업 파이썬 기초문제 66
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if (a % 2) == 0:
    print('even')
else:
    print('odd')
if (b % 2) == 0:
    print('even')
else:
    print('odd')
if (c % 2) == 0:
    print('even')
else:
    print('odd')

#코드업 파이썬 기초문제 67
a=int(input())

if (a<0):
    if(a % 2 == 0):
        print('A')
    else:
        print('B')
else:
    if(a % 2 == 0):
        print('C')
    else:
        print('D')

#코드업 파이썬 기초문제 68
a=int(input())

if (a<40):
    print('D')
elif (a<70):
    print('C')
elif (a<90):
    print('B')
elif (a<=100):
    print('A')

#코드업 파이썬 기초문제 69
a=input()

if (a=='A'):
    print('best!!!')
elif (a=='B'):
    print('good!!')
elif (a=='C'):
    print('run!')
elif (a=='D'):
    print('slowly~')
else:
    print('what?')

#코드업 파이썬 기초문제 70
a=int(input())

if (a//3==1):
    print('spring')
elif (a//3==2):
    print('summer')
elif (a//3==3):
    print('fall')
else:
    print('winter')

#코드업 파이썬 기초문제 71
a=1

while a!=0:
    a=int(input())
    if(a != 0):
        print(a)

#코드업 파이썬 기초문제 72
a=int(input())

while a!=0:
    print(a)
    a=a-1

#코드업 파이썬 기초문제 73
a=int(input())

while a!=0:
    a=a-1
    print(a)
    
#코드업 파이썬 기초문제 74
a=ord(input())
c=ord('a')
while c<=a:
    print(chr(c), end=' ')
    c=c+1

#코드업 파이썬 기초문제 75
a=int(input())
c=0
while c<=a:
    print(c)
    c=c+1

#코드업 파이썬 기초문제 76
a=int(input())

for i in range(a+1):
    print(i)

#코드업 파이썬 기초문제 77
a=int(input())
b=0
for i in range(1, a+1):
    if (i%2)==0:
        b=b+i
print(b)

#코드업 파이썬 기초문제 78
while 1:
    a=input()
    if a!='q':
        print(a)
    else:
        print(a)
        break

#코드업 파이썬 기초문제 79
a=int(input())
b=0

for i in range(1,a+1):
    b=b+i
    if b>=a:
        print(i)
        break

#코드업 파이썬 기초문제 80
a,b=input().split()
a=int(a)
b=int(b)

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i,j)

#코드업 파이썬 기초문제 81
a=int(input(),16)

for i in range(1,16):
    print('%X'%a,'*%X'%i,'=%X'%(a*i),sep='')

#코드업 파이썬 기초문제 82
a=int(input())

for i in range(1,a+1):
    if (((i%10)%3==0) and i%10!=0):
        print('X', end=' ')
    else:
        print(i, end=' ')
    
#코드업 파이썬 기초문제 83
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
count=0
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            count=count+1
            print(i,j,k,sep=' ')
print(count)

#코드업 파이썬 기초문제 84
a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
f=a*b*c*d
g=f/8/1024/1024
print('%.1f'%g,'MB')

#코드업 파이썬 기초문제 85
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
f=a*b*c
g=f/8/1024/1024
print('%.2f'%g,'MB')

#코드업 파이썬 기초문제 86
a=int(input())
j=0
for i in range(1,a+1):
    j=j+i 
    if (j>=a):
        print(j)
        break
        
#코드업 파이썬 기초문제 87
a=int(input())

for i in range(1,a+1):
    if(i%3!=0):
        print(i,end=' ')

#코드업 파이썬 기초문제 88
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
count=1

while 1:
    if (count >= c):
        print(a)
        break
    a=a+b
    count=count+1

#코드업 파이썬 기초문제 89
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
count=1

while 1:
    if (count >= c):
        print(a)
        break
    a=a*b
    count=count+1

#코드업 파이썬 기초문제 90
a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
count=1

while 1:
    if (count >= d):
        print(a)
        break
    a=a*b+c
    count=count+1

#코드업 파이썬 기초문제 91
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=1

while ((d%a!=0) or (d%b!=0) or (d%c!=0)):
    d=d+1
print(d)

#코드업 파이썬 기초문제 92
n=int(input())

num=[]
a=input().split()
for i in range(n):
    a[i]=int(a[i])

for i in range(24):
    num.append(0)

for i in range(n):
    num[a[i]]=num[a[i]]+1

for i in range(1,24):
    print(num[i],end=' ')

#코드업 파이썬 기초문제 93
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

for i in range(n-1,-1,-1):
    print(a[i],end=' ')

#코드업 파이썬 기초문제 94
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

c=a[0]
for i in range(0,n):
    if (c>=a[i]):
        c=a[i]
        
print(c)

#코드업 파이썬 기초문제 95
n=int(input())

a=[[0 for i in range(20)] for j in range(20)]

for p in range(n):
    x,y = input().split()
    x=int(x)
    y=int(y)

    a[x][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end=' ')
    print('')

#코드업 파이썬 기초문제 96
d = [[0 for j in range(20)] for i in range(20)]

for i in range(1, 20):
        a = [int(x) for x in input().split()]
        for j in range(1,20):
            d[i][j] = a[j-1]
        
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(1,20):
        if d[x][j] == 0 :
            d[x][j] = 1
        else :
            d[x][j] = 0
            
        if d[j][y] == 0 :
            d[j][y] = 1
        else :
            d[j][y] = 0
    
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print() 

#코드업 파이썬 기초문제 97
h,w=map(int,input().split()) #판 크기
n=int(input()) #막대 개수

base=[[0 for i in range(h)] for j in range(w)]

for i in range(n):
    l,d,x,y=map(int,input().split())
#l:길이 d:방향(가로0세로1) x,y:좌표
    for j in range(l):
        if (d==0):
            base[(y-1)+j][x-1]=1
        elif(d==1):
            base[y-1][(x-1)+j]=1

for i in range(h):
    for j in range(w):
        print(base[j][i],end=' ')
    print()

#코드업 파이썬 기초문제 98
base=[[int(i) for i in input().split()] for j in range(10)]
x,y=1,1
base[x][y]=9
while 1:
    if(base[x][y+1]==0):
        base[x][y+1]=9
        y+=1
    elif(base[x][y+1]==1):
        if(base[x+1][y]==1):
            break
        elif(base[x+1][y]==0):
            base[x+1][y]=9
            x+=1
        elif(base[x+1][y]==2):
            base[x+1][y]=9
            break
    elif(base[x][y+1]==2):
        base[x][y+1]=9
        break
    
for i in range(len(base)):
    for j in range(len(base)):
        print(base[i][j],end=' ')
    print()