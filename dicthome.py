x={"java":{"spring":[70,80,90],"struts":[78,65,57],"jsf":[89,45,38]},
   "python":{"django":[99,89,95],"flask":[78,56,76],"pyramid":[56,67,54]},
   "hadoop":{"hive":[89,67,78],"pig":[84,37,54],"sqoop":[99,78,24]}}
for  i,j in x.items():
    total=0
    for a,b in j.items():
      s=0
      for c in b:
          s=s+c
      print(s)
      total=total+s
    print(total)
    print("----")


#membership operators only work on the keys
'''y= {'java':"django","python":"flask","hadoop":"hive"}
p=input("enter the search element")
if p in y:
    print("element is found")
else:
    print("element is not found")'''
    
#Directory comprehension:
x={p*p for p in range(5)}
print(x)
y={p*p*p for p  in range(10)}
print(y)
z={r**3 for r in range(12)}
print(z)
E={p*p for p in range(10,20) if p%2==0}
print(E)
#leap year in python
'''x=int(input("enter the year" ))
if ((x%400==0) or ((x%100!=0)and(x%4==0)))
else:
    print("This is not leap year")'''
#words count
line="python djangao restapi lokesh"
words=line.split()
x={(len(w),w.upper(),w.lower()) for w in words}
print(x)
print(help(tuple))
#how too add dictionar values
x={"python":90,"java":80,"hadoop":82}
y={"java":82,"hadoop":86,"python":98}
z=x.update(y)
print(z)

#how to print dictionary values
ks = {k for k in x.keys()}
print(ks)
d_merged = {k:(x[k],y[k]) for k in ks}
print(d_merged)











