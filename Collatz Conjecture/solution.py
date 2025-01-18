def steps(number):
    counter=0
    if number<= 0 :
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1:
            counter += 1
            if number % 2 == 0:
                number//=2
            else:
                number= number * 3 + 1
    return counter

try:
    x = input("Enter a positive integer: ")
    result = steps(int(x))
    print(f"Number of steps: {result}")
except ValueError as e:
    print(f"Error: {e}")