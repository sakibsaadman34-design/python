x = 35

if (type(x) is int):
    print("true")
else:
    print("false")

x = 6.7

if (type(x) is not float):
    print("True")
else:
    print("False")

a = 30

b = 30

if (a is b):
    print("a and b has same identity")
else:
    print("a and b has different identity")

a = 25

b = 30

if (a is not b):
    print("a and b has different identity")
else:
    print("a and b has same identity")