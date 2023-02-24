operations = ["*", "+", "-", "/"]

def make_operation(nr):
    op_flag = True
    second_nr_flag = True
    result = 0
    zero_protection = False
    while op_flag:
        operation = input("Pick an operation from the list(* / + -):   ")
        if operation in operations:
            op_flag = False
        else:
            print("That is not an operation from the list")

    while second_nr_flag:
        second_nr = input("What's the next number?:   ")
        try:
            float(second_nr)
            second_nr_flag = False
        except:
            print("This is not a valid number")
            second_nr_flag = True

    nr = float(nr)
    second_nr = float(second_nr)
    if operation == "*":
        result = nr * second_nr
    elif operation == "+":
        result = nr + second_nr
    elif operation == "-":
        result = nr - second_nr
    elif operation == "/":
        if second_nr == 0:
            print("Cant divide by zero. No operation will be done")
            result = nr
            zero_protection = True
        else:
            result = nr / second_nr

    if zero_protection is False:
        print(f"{nr} {operation} {second_nr} = {result}")
    else:
        print(f"Your number is {sum}")


while True:
    number = input("What's the first number?: ")
    try:
        float(number)
    except:
        print("This is not a valid number")
        continue
    make_operation(number)







