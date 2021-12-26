#dict important problems
x={"java":80,"python":99,"hadoop":78}
print(x)
y=x.items()
for p in y:
   for q in p:
        print(q,end=" ")
   print() 
#another way
for i,j in y:
  print(i,j)
  print("")
#sum
x={"java":[80,82,73],"python":[90,67,43],"hadoop":[78,65,90]}
print(x)
print()
for k in x:
    print(k,end="")
    v=x[k]
    s=0
    for p in v:
        s=s+p
    print(s)
#for with unpacking
y={"java":[80,90,76],"python":(99,78,98),"hadoop":{78,87,77}}
print(x)
for k,j in x.items():
    print(k,end=" ")
    s=0
    for q in j:
      s=s+q
    print(s)
    
x={"sarada":[78,90,54],"kumar":[23,45,67],"sagar":[76,54,32]}
for i,j in x.items():
    print(i,end="  ")
    s=0
    for k in j:
        s=s+p
    print(s)
#another way
x={(90,82,73):"java",(99,96,97):"python",(76,65,43):"hadoop"}
print(x)
for k,j in x.items():
    s=0
    for q in k:
      s=q+s
    print(s,j)
#Nested Dictionaries
x={"java":{"spring":90,"struts":80,"jsf":67},"python":{"django":98,"flask":67,"pyramid":48},"hadoop":{"hive":89,"pig":91,"sqoop":78}}
print(x)
for i in x:
    print(i,x[i])
    for j in x[i]:
      print(x[i][j])

for i,j in x.items():
    print(i,j)
    for a,b in j.items():
        print(a,b)
print(" ")
#Nested dictionary5
x={"java":{"spring":[70,80,90],"struts":[78,65,57],"jsf":[89,45,38]},"python":{"django":[99,89,95],"flask":[78,56,76],"pyramid":[56,67,54]},"hadoop":{"hive":[89,67,78],"pig":[84,37,54],"sqoop":[99,78,24]}}
for i,j in x.items():
   print(i,j)
   for a,b in j.items():
     print(a,b)
     for c in b.items( ):
        print(c)





        
        
