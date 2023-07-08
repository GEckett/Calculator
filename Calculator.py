import os
from art import logo 

#add function
def add(n1,n2):
    return n1 + n2

#sub function
def sub(n1,n2):
    return n1 - n2

#multi function
def multi(n1,n2):
    return n1 * n2

#div function
def div(n1,n2):
    return n1 / n2

#function dictionary
operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

#calc function

def calculator():
    Calc_off = False
    answer = 0
    print(logo)
    while not Calc_off: 
        if answer == 0:
            num1 = float(input("First number?"))
        else:
            num1 = answer
        num2 = float(input("Next number?"))
        for symbol in operations:
            print(symbol)
        op_symbol = input("Pick one of the above operations")
        if op_symbol not in operations:
            print("ERROR - FUNCTION NOT FOUND")
        else:
            calc_function = operations[op_symbol]
            answer = calc_function(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        Calc_cont = input(f"Do you want to perform anouther calculation on {answer}? Yes or No.").lower()
        if Calc_cont == "no":
            Calc_off = True
            os.system('cls||clear')
            calculator() 
        else:
            os.system('cls||clear')

#Calc Kickoff

print(logo)
calculator()

