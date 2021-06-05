num = int(input())
han = False
count=0
x=[]
for i in range(1,num+1):
    [x.append(j) for j in str(i)]
    for k in range(len(x)-1):
        if(len(x)!=1):
            a=int(x[k+1])-int(x[k])
        if (len(x)==1 or (int(x[k])+a)==x[k+1]):
            han = True
    if(han==True):
        count+=1
        han=False
    x.clear() 

print(count)