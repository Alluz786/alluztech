print("CALCULATOR")

print('''
 DEVOLOPED BY AL AMEEN HUSAIN

 '''
 )

a= float(input("ENTER A  VALUE==>"))
op= input("SELECT A OPERATOR(+-×/)")
b= float(input("ENTER A SECOND VALUE==>"))

if(op=='+'):
  print(a+b)
elif(op=='-'):
  print(a-b)
elif(op=='*'):
  print(a*b)
else:
 print(a/b)
