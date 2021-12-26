x={"java":78,"python":54,"spring":12}
print(x)
y=x.keys()
print(y)
for p in y:
    print(p)
z={"sarda":23,"hema":26,"sai":67}
print(z)
v=z.values()
print(v)
for j in v:
    print(j)
c=z.items()
print(c)
for k in c:
    print(k)
    for i in k:
        print(i)
#vegtables data
A={"reliance":15,"tesla":78,"facebook":45,"instagram":54,"phonepay":75}
print(A)
B=A.items()
for i in B:
    print(i)
C={"MCA":3,"B.Sc":3,"Inter":2,"10th":1}
print(C)
D=C.items()
for p in D:
    print(p)
    for q in p:
     print(q)

Z=C.keys()
print(Z)
Y=C.values()
print(Y)
#print the key values
D={"onion":89,"tomoto":78,"beetroot":80,"carrot":67}
C=D.items()
print(C)
for p in C:
    for q in p:
        print(q,end=" ")
    print()

E={"computer":88,"ipod":90,"iphone":67,"telephone":76}
F=E.items()
print(F)
for p in F:
   for q in p:
    print(q,end="")
   print()
print()
for i,j in F:
    print(i,j)
#sum of values
x={"apples":90,"banana":89,"litch":40,"pineapple":78}
y=x.items()
print(y)
for i in y:
    print(i,end=" ")
    j=y[i]
    s=0
    for p in j:
        s=s+p
    print(s)
    
    
