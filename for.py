x=range(10)
print(x)
print(x[2])
print(x[-2])
for p in x:
    print(p)
#while range
x=range(10,20)
print(x)
print(len(x))
i=0
while i <len(x):
    print(x[i])
    i = i+1
#range with step
'''x=range(20,30,2)
print(x)
print(len(x))
i=0
while i<=len(x):
    print(x[i])
    i=i+1'''
#for loop with range
x=range(20,30)
print(len(x))
for p in x:
    print(p)
    
     
    
y=range(-30,-20,3)
print(y)
print(len(y))
print(y)
for q in y:
    print(q)
#for loop sum
'''s=0
for p in range(1,200):
  s= s + p
print(s)
x = int(input("enter the table number: "))
for p in range(1,11):
    print(p,"*",x,"=",p*x)'''
        
#matrix multiplication operator
x=[[1,5,4],[2,3,4],[5,4,7]]
y=[[4,8,7],[5,8,9],[2,1,4]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
         for k in range(len(y)):
            result[i][j]=result[i][j] + (x[i][k]*y[k][j])
for z in result:
print(z)









