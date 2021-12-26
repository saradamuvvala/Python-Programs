x= 1000
print(x)
print(type(x))
print(id(x))

x = 2000
print(x)
print(type(x))
print(id(x))


#mutable objects

i = [12,32,45]
print(i)
print(type(i))
print(id(i))
i[1] = 99
print(i[1])
i[2] = 89
print(i)

#mutable objects
y = "sarada"
print(y)
print(y[2])
print(y[-5])

#Reading the data from keyboard
'The data read from the keyboard we use the input() function'
#type conversion functions
#int,float,complex,bool
'''a = input("enter the name")
print(a)
b = input("enter the surname")
print(b)
print(a + b)'''
#using type conversion int
'''c = input("enter the first number")
print(c)
print(type(c))
d = int(c)
print(d)
print(type(d))'''
#using type conversion float
'''e = input('enter the first value')
print(e)
print(type(e))
d = float(e)
print(type(d))
print(d)'''
#using type conversion complex
'''x = input('enter the number')
print(x)
print(type(x))
z=complex(x)
print(type(z))
print(z)'''
#using type conversion bool
j = input("enter the value")
print(j)
print(type(j))
k=bool(j)
print(type(k))
print(k)

