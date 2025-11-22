import sys

# Expecting 5 marks as arguments
if len(sys.argv) < 6:
    print("usage: python average.py <mark1> <mark2> <mark3> <mark4> <mark5>")
    sys.exit(1)

# Convert arguments to integers
marks = [int(sys.argv[i]) for i in range(1, 6)]

# Calculate average
average = sum(marks) / 5

print("Marks:", marks)
print("Average:", average)

# Grade logic
if average >= 40:
    print("You Passed.")
else:
    print("You Failed.")
