# 1. Get measurements in cm
length = float(input("Enter the length of the rectangle (cm): "))
width = float(input("Enter the width of the rectangle (cm): "))

# 2. Calculate the area
correct_area = length * width

# 3. Ask for the guess
user_guess = float(input("What is the area of this rectangle? "))

# 4. Check the answer and show the unit
if user_guess == correct_area:
    print(f"Correct! The area is {correct_area} cm².")
else:
    print(f"Not quite. The correct area was {correct_area} cm².")
