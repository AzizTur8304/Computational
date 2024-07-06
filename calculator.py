# Function for the calculator
def calculator(key, value1, value2):
    value1 = float(value1)
    value2 = float(value2)
    if key == '*':
        return value1 * value2
    elif key == '/':
        return value1 / value2
    elif key == '+':
        return value1 + value2
    elif key == '-':
        return value1 - value2
    else:
        return "Invalid key!"

# Displaying the calculator layout
dict = {
    1: [" ", " ", " ", " "],
    2: ["Lock", '/', '*', '-'],
    3: [7, 8, 9, '+'],
    4: [4, 5, 6, ' '],
    5: [1, 2, 3, 'Enter'],
    6: [' ', '0', '.', ' ']
}

for key, value in dict.items():
    num1, num2, num3, num4 = value
    print("{:>6} {:>6} {:>6} {:>6}".format(num1, num2, num3, num4))

validCompute = ['/', '*', '-', '+']

n = input("Please enter a number: ")
n = float(n)

while True:
    m = input("Please enter a computational character (+, -, *, /): ")
    if m not in validCompute:
        print("Invalid computational character! Please try again.")
        continue

    k = input("Please enter another number: ")
    try:
        k = float(k)
    except ValueError:
        print("Invalid number! Please try again.")
        continue

    result = calculator(m, n, k)
    print(f"The result of {n} {m} {k} is: {result}")
    n = result

    Continue = input("Do you want to continue? (yes/no): ").lower()
    if Continue == 'no':
        break
    elif Continue != 'yes':
        print("Invalid response, exiting.")
        break
