
OUT_OF_BOUNDS =float('-inf')
# print(OUT_OF_BOUNDS)



def calculate(first_number, second_number, operator):
    result = 0
    if operator == "+":
        result = (first_number + second_number)
    elif operator  == "-":
        result = (first_number - second_number)
    elif operator  == "*":
        result = (first_number * second_number)
    elif operator  == "/":
        result = (first_number / second_number)
    else:
        result =OUT_OF_BOUNDS
    return result
# print  (calculate(1,2,"+"))
more_input = True
while more_input:
    first_number = input("what is the first number to add?")
    first_number = int(first_number)

    second_number = input("what is the second number to add?")
    second_number = int(second_number)
    print(first_number, second_number)
    print(first_number +second_number)
    operator = input ("what operation do you want me to do(+, -, *, /)?")

    result = calculate(first_number , second_number, operator)

    if result ==OUT_OF_BOUNDS:
        print("you need a valid operator(+, -, *, /)")

    else:
        print(result)
    if input("Another calculation (y/n)? ") == "y":
        more_input =True 
    else:
        more_input =False

