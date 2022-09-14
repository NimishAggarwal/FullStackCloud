print("hello world")
number1= 12
number2= 18
name1= "hello"
name2= "world"
total=number1+number2
print(total)
print(name1+name2)
#my_test_variable
#print(my_test_variable)
print("test",total)
var=None
my_integer_var=1000
my_float_var=3.5
my_complex_var=1.2

print(type(my_integer_var))
print(type(var))
print(2**3) #power
print(2*4) #multiply
print(4/2) #quotient
print(5%2) #remainder

print(name1+name2)
print("hello"+"world")
name2+=name1
print(name2)
print("nimish".join("hello"))

from io import StringIO
concat=StringIO()
concat.write("nimish")
concat.write("hello")
print(concat.getvalue())
