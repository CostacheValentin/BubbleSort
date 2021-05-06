def selection(x):
    for i in range(0,len(x)-1):
        k=i
        for j in range(i+1,len(x)):
            if x[k]>x[j]:
                k=j
        if k!=i:
            aux=x[i]
            x[i]=x[k]
            x[k]=aux
    return x
x=[2,1,4,5,3,0]
print selection(x)
