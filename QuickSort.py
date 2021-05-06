import random

def quicksort1(x,s,d):
    if s<d:
        q,cp=pivot1(x,s,d)
        c1=quicksort1(x,s,q-1)
        c2=quicksort1(x,q+1,d)
        c=c1+c2+cp
    else:
        c=0
    return c

def pivot1(x,s,d):
    v=x[d]
    i=s-1
    j=d
    c=0
    while i<j:
        while True:
            i+=1
            c+=1
            if x[i]>=v:
                break
        while True:
            j-=1
            c+=1
            if x[j]<=v:
                break
        if i<j:
            x[i],x[j]=x[j],x[i]
    x[i],x[d]=x[d],x[i]
    return i,c


x=[]
for i in range(0,150000):
    x.append(random.randint(-9999,9999))
    
print "Comparatii Quicksort p1= ",quicksort1(x,0,len(x)-1)


