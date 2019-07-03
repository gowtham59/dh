vj1,vs2=map(int,input().split())
v3=[]
s4=[]
a5=[int(vj1) for vj1 in input().split() ]
for i in range(0,vs2):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        s4.append(a[j])
    x=sorted(s4)
    v3.append(min(s4))
    del s4[:]
for sz in range(0,len(v3)):
    print(v3[sz])
