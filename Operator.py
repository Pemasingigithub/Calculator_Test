#Calculator 1: Using class , object , function[method] and  inheritance
class Calculator:
    def __init__(self,n1,n2):#Initilize the properties
        self.number1=n1
        self.number2=n2
class Add(Calculator):
    pass
    def addition(self):
       return self.number1+self.number2 #Addtion

class Sub(Add):
    pass
    def subtraction(self):
      return self.number1-self.number2 #Subtraction

class Mul(Sub):
    pass
    def multiplication(self):
      return self.number1*self.number2 #Multiplication


class Div(Mul):
    pass
    def division(self):
      return self.number1/self.number2 #Divison

n1 = int(input("Enter first number:_"))  # Input first number
n2 = int(input("Enter the second number:_"))  # Input second number

#object created
a=Add(n1,n2)  # Parameter pass
s=Sub(n1,n2)
m=Mul(n1,n2)
d=Div(n1,n2)

while True:
    print("What do you want?")
    option_input=("1.Addition\n2.Subtract\n3.Mulply \n4.Divide ")
    print(option_input)

    try:
     select_number=int(input("Select the above option:_"))
    except ValueError:
             exit("Give only integer value")



    if select_number==1:
            print("Result is:",a.addition())


    elif select_number==2:
            print("The result is:",s.subtraction())


    elif select_number==3:
            print("The result is:",m.multiplication())


    elif select_number==4:
            print("The result is:",d.division())


    else:
            print("Invalid option")
            break


# Calculator 2: Using class , function , object
class Cal:
    def calculation(self):
      self.num1=int(input("Enter number 1:_"))
      self.num2=int(input("Enter number 2:_"))
      operator_choose=input("choose operator:['+','-','*','/']_")
      if operator_choose=='+':
         return print("The sum is:",self.num1+self.num2)
      elif operator_choose=='-':
         return print("The subtract is:", self.num1 - self.num2)

      elif operator_choose=='*':
         return print("The multiplication is:", self.num1 * self.num2)

      else:
         return print("The devide is:", self.num1 / self.num2)

print("Now next other method of calculator")
c=Cal()
c.calculation()
def exit_method():
    yesno=input("Do you want continue[y or n]:_")
    if yesno=='y' or yesno=='Y':
        c.calculation()
        exit_method()
    else:
        print("Exit program")
exit_method()





















