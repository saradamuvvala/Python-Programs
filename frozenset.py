#frozensete
x=[10,20,30,40,56,7,8]
print(x)
y=frozenset(x)
print(y)
print(type(y))
print(len(y))
#copy frozenset
z=y.copy()
print(z)
u=y.copy()
print(u)
x=y.copy()
print(x)
#union of frozenset
q=(34,56,78,32,90,7,8,9,90)
p=frozenset(q)
print(p)
print(type(p))
print(p.union(x))
print(p.intersection(x))
print(p.isdisjoint(x))
print(p.difference(x))
print(p.symmetric_difference(x))
#searching an element using the frozenset
'''r=[45,6,7,89,898,9,90,"sarada"]
s=frozenset(r)
print(r)
z=(input("enter an element"))
if z in r:
    print("element is found")
else:
    print("element is not found")'''
#searching an element using the frozenset
'''z=[78,89,46,"sarada","hema","juhi","anup","sagar"]
y=frozenset(z)
print(z)
j=input("enter the element")
if j in z:
    print("element is found")
else:
    print("element is not found")'''
#unpacking of elements
'''x=[45,67,32,"sarada"]
y=frozenset(x)
print(y)
a,b,c,d =y
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))'''
#print of array
x=[(2,3,4),(6,7,8),(2,3,5,56)]
z=frozenset(x)
print(z)
for i in z:
 print(i)

z=[(6,8,7,),(8,9,6),(3,4,5),(2,4,6)]
x=frozenset(z)
print(x)
for p in x:
    for q in p:
        print(q,end=" ")
    print()
print()
p=[(7,8,9),(5,6,7),(5,8,7)]
q=frozenset(p)
for a,b,c in q:
    print(a,b,c)






