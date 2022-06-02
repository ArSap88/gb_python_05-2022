def to_divide(first, second):
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(to_divide(int(input("Enter dividend = ")), int(input("Enter divider = "))))
