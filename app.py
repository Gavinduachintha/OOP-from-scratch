print("Calculator using OOP method in python")
class Calculator:
    # def __init__(self):
    #     print("Calculator using OOP")
    
    def add(self,a,b)->int:
        return a+b
    
    def subtract(self,a,b)->int:
        return a-b

    def multiplication(self,a,b)->int:
        return a*b
    
    def divide(self,a,b)->float|str:
        if b==0:
            return("Error dividing 0")
        else:
            return(a/b)

calc = Calculator()

running = True
while running:
    print("Enter your choice: ")
    print("1 - Add")
    print("2 - Substract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")
    userInput=int(input("Enter your choice: "))

    if(userInput==5):
        print("Exiting")
        break
    else:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))

        if(userInput==1):print("Addition: ", calc.add(a,b))
        elif(userInput==2):print("Subtraction: ", calc.subtract(a,b))
        elif(userInput==3):print("Multiplication: ",calc.multiplication(a,b))
        elif(userInput==4):print("Division: ",calc.divide(a,b))
        print("\n")

