#print even numbers
'''print("begin")
x = input("enter the value")
y = int(x)
z=abs(y)
print(z)
if z%2==0:
    print(z,"is a even value")
else:
    print(z,"is a odd value")
print("end")'''
#print while loop
'''print("begin")
x = input("enter the value")
y= int(x)
z=abs(y)
if z<10:
   print(z,"is a even value")
elif z<=100:
   print(z,"is a 2 digit value")
elif z<=1000:
   print(z,"is a 3 digit value")
else:
   print(z,"is a large value")
print("end")'''
#print while loop
'''print("begin")
i=0
while i<=5:
   print("welcome",i)
   i=i+1
print("end")'''
#print sum of values
'''print("begin")
i = int(input("enter begin value"))
s=0
j= int(input("enter last value"))
while i <= j:
   if i%2==0: 
      s=s+i
   i=i+1
print(s)
print("end")'''
#print of remove duplicate values from list
my_list = [23,45,6,7,8,9,67,8,9,7]
print(my_list)
result_list=[]
for i in my_list:
   if i not in result_list:
      result_list.append(i)
   print(result_list)
print("end")
















   
