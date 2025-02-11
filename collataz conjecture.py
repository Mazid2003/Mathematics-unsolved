def collatz_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    steps = 0
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    
    print(1)  # Print the last step when reaching 1
    print(f"Total steps: {steps}")

# Example Usage
number = int(input("Enter a positive integer: "))
collatz_sequence(number)
