print("Enter marks obtained in 5 subjects")

Mark1 = int(input("Enter number in subject 1"))

Mark2 = int(input("Enter number in subject 2"))

Mark3 = int(input("Enter number in subject 3"))

Mark4 = int(input("Enter number in subject 4"))

Mark5 = int(input("Enter number in subject 5"))

tot = Mark1 + Mark2 + Mark3 + Mark4 + Mark5

avg = int(tot / 5)

ValidRange = range(0, 101)

if (avg not in ValidRange):

    print("Invalid Input")

elif avg in range(91, 101):

    print("A1")

elif avg in range(81, 91):

    print("A2")

elif avg in range(71, 81):

    print("B1")

elif avg in range(61, 71):

    print("B2")

elif avg in range(51, 61):

    print("C1")

elif avg in range(41, 51):

    print("C2")

elif avg in range(31, 41):

    print("D1")

elif avg in range(21, 31):

    print("D2")

elif avg in range(11, 21):

    print("F1")

elif avg in range(0, 11):

    print("F2")