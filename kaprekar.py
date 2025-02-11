def kaprekar_6174(num):
    if num < 1000 or num > 9999:
        print("Please enter a four-digit number.")
        return
    
    if len(set(str(num))) == 1:  # Check if all digits are the same
        print("All digits are the same. No valid Kaprekar process.")
        return
    
    steps = 0
    while num != 6174:
        digits = [int(d) for d in str(num).zfill(4)]  # Ensure 4 digits, even for numbers like 100
        large = int("".join(map(str, sorted(digits, reverse=True))))
        small = int("".join(map(str, sorted(digits))))
        num = large - small
        steps += 1
        print(f"Step {steps}: {large} - {small} = {num}")
    
    print(f"Reached 6174 in {steps} steps!")

# Example Usage
if __name__ == "__main__":
    number = int(input("Enter a four-digit number: "))
    kaprekar_6174(number)
