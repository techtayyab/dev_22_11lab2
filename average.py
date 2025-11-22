import sys

if len(sys.argv) < 6:
    print("No marks provided, using defaults...")
    marks = [10, 20, 30, 40, 50]
else:
    marks = list(map(int, sys.argv[1:6]))

avg = sum(marks) / len(marks)
print("Average:", avg)

# Fail if average is less than 40
if avg < 40:
    print("Build failed: average is below 40")
    sys.exit(1)
else:
    print("Build passed")
    sys.exit(0)
