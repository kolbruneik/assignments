age = int(input("Enter your age: "))

if age in range(0, 34):
    print("Young")
elif age in range(35, 50):
    print("Mature")
elif age in range(51, 69):
    print("Middle-aged")
elif age >= 70:
    print("old")
else:
    print("Invalid age")
