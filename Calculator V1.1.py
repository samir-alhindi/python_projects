def add_numbers(number_1:float , nummber_2:float):
    sum: float = (number_1 + nummber_2)
    return sum
    
def subtract_numbers(number_1:float , nummber_2:float):
    difference: float = (number_1 - nummber_2)
    return difference

def multiply_numbers(number_1:float , nummber_2:float):
    multiplication: float = (number_1 * nummber_2)
    return multiplication

def divide_numbers(number_1:float , nummber_2:float):
    answer: float = (number_1 / nummber_2)
    return answer


print("---------------------------------------")
print("---------Samir's Caluculator-----------")
print("---------------------------------------")

number_1: float = float(input("Please enter the 1st number here: "))
nummber_2: float = float(input("Please enter the 2nd number here: "))

print("-------------------------------------")

operation = input("Enter 1 for Addition '+'\nEnter 2 for Subtraction '-'\nEnter 3 for Multiplication '*'\nEnter 4 for Division '/'")

if operation == "1":
    print("Sum is: " + str(add_numbers(number_1 , nummber_2)))
elif operation == "2":
    print("Difference is: " + str(subtract_numbers(number_1 , nummber_2)))
elif operation == "3":
    print("Multiplication is: " + str(multiply_numbers(number_1 , nummber_2)))
elif operation == "4":
    print("Result is: " + str(divide_numbers(number_1 , nummber_2)))
else:
    print("Invalid operation, Please try again.")

    
