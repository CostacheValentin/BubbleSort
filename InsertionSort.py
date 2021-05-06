def insertion(x):
    for i in range(1,len(x)):
        aux=x[i]
        j=i-1
        while j>=0 and aux<x[j]:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=aux
    return x
x=[2,1,4,5,3,0]
print insertion(x)

