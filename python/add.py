import sys

total = 0
for number in sys.argv[1:]:
    total += float(number)

print total
