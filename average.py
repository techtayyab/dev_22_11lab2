import sys

# List to store marks for each subject
marks = []

# Get individual marks for 5 subjects
for i in range(5):
    while True:
        try:
            mark = input(f"Enter the mark for subject {i+1}: ")
            # Try to convert input to an integer
            marks.append(int(mark))
            break  # If input is valid, break out of the loop
        except ValueError:
            # If input is not a valid integer, ask again
            print(f"Invalid input! '{mark}' is not a valid integer. Please enter a valid mark.")

# Calculate the average of the marks
avg = sum(marks) / len(marks)
print(f"Average: {avg:.2f}")

# Fail if average is less than 40
if avg < 40:
    print("Build failed: average is below 40")
    sys.exit(1)
else:
    print("Build passed")
    sys.exit(0)
