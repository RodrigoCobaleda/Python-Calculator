ask = """type 'add' for addition,
type 'sub' for subtracting,
type 'div' for divising (normal),
type 'mult' for multiplying"""
#presents the info









print(ask)
method = input("type the method\n")
N1 = float(input("type first number\n"))
N2 = float(input("type second number\n"))
#values 
  





def calculator(Met,Num1,Num2):
  if method == "add":
    add = N1+N2
    print(add)
  elif method == "sub":
    sub = N1-N2
    print(sub)
  elif method == "div":
    div = N1/N2
    print(div)
  elif method == "mult":
    mult = N1*N2
    print(mult)
#actual calculator function




    
calculator(method,N1,N2)






