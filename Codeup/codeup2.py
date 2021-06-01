#코드업 파이썬 기초문제 31
a=int(input())
print(chr(a))

#코드업 파이썬 기초문제 32
a=int(input())
print(-a)

#코드업 파이썬 기초문제 33
a=ord(input())
print(chr(a+1))

#코드업 파이썬 기초문제 34
a,b=input().split()
c=int(a)-int(b)
print(c)

#코드업 파이썬 기초문제 35
a,b=input().split()
c=float(a)*float(b)
print(c)

#코드업 파이썬 기초문제 36
a,n=input().split()
print(a*int(n))

#코드업 파이썬 기초문제 37
n=input()
a=input()
print(a*int(n))

#코드업 파이썬 기초문제 38
a,b=input().split()
c=int(a)**int(b)
print(c)

#코드업 파이썬 기초문제 39
a,b=input().split()
c=float(a)**float(b)
print(c)

#코드업 파이썬 기초문제 40
a,b=input().split()
c=int(a)//int(b)
print(c)

#코드업 파이썬 기초문제 41
a,b=input().split()
c=int(a)%int(b)
print(c)

#코드업 파이썬 기초문제 42
a=float(input())
print(format(a, ".2f"))

#코드업 파이썬 기초문제 43
a,b=input().split()
c=float(a)/float(b)
print(format(c, ".3f"))

#코드업 파이썬 기초문제 44
a,b=input().split()
c=int(a)+int(b)
print(c)
c=int(a)-int(b)
print(c)
c=int(a)*int(b)
print(c)
c=int(a)//int(b)
print(c)
c=int(a)%int(b)
print(c)
c=int(a)/int(b)
print(format(c,".2f"))

#코드업 파이썬 기초문제 45
a,b,c=input().split()
d=int(a)+int(b)+int(c)
e=d/3
print(d,format(e,".2f"))

#코드업 파이썬 기초문제 46
a=int(input())
print(a<<1)

#코드업 파이썬 기초문제 47
a,b=input().split()
print(int(a)<<int(b))

#코드업 파이썬 기초문제 48
a,b=input().split()
print(int(a)<int(b))

#코드업 파이썬 기초문제 49
a,b=input().split()
print(int(a)==int(b))

#코드업 파이썬 기초문제 50
a,b=input().split()
print(int(b)>=int(a))

#코드업 파이썬 기초문제 51
a,b=input().split()
print(int(b)!=int(a))

#코드업 파이썬 기초문제 52
a=int(input())
print(bool(a))

#코드업 파이썬 기초문제 53
a=bool(int(input()))
print(not a)

#코드업 파이썬 기초문제 54
a,b=input().split()
print(bool(int(a)) and bool(int(b)))

#코드업 파이썬 기초문제 55
a,b=input().split()
print(bool(int(a)) or bool(int(b)))

#코드업 파이썬 기초문제 56
a,b=input().split()
a=bool(int(a))
b=bool(int(b))
print((a == (not b)) and (b == (not a)))

#코드업 파이썬 기초문제 57
a,b=input().split()
a=bool(int(a))
b=bool(int(b))
print((a or(not b)) and (b or(not a)))

#코드업 파이썬 기초문제 58
a,b=input().split()
a=bool(int(a))
b=bool(int(b))
print((not b) and (not a))

#코드업 파이썬 기초문제 59
a=int(input())
print(~a)

#코드업 파이썬 기초문제 60
a,b=input().split()
print(int(a)&int(b))