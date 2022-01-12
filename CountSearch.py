def countSort(a):
    acc=[]
    for i in range(101):
        acc+=[0]
    for i in a:
        acc[i]+=1
    j=0
    for i in range(101):
        if acc[i]>0:
            for k in range(acc[i]):
                a[j]=i
                j+=1