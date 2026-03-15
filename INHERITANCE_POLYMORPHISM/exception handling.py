# Exception handling

try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a + b
    print("The result:", c)
except ValueError as e:
    print("Value Error:", e)
except NameError as e:
    print("Name Error:", e)
except TypeError as e:
    print("Type Error:", e)
finally:
    print("Done")