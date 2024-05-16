# Define variables a and b on separate lines
a = 10
b = 5

# Import required functions from calculator_1.py
from calculator_1 import add, sub, mul, div

def main():
    # Perform calculations using the imported functions
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    # Print the results, ensuring no more than four print calls
    print(f"{a} + {b} = {addition_result}")
    print(f"{a} - {b} = {subtraction_result}")
    print(f"{a} * {b} = {multiplication_result}")
    print(f"{a} / {b} = {division_result}")

if __name__ == "__main__":
    main()

