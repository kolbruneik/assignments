integer = int(input("Enter an integer: "))
counter_odd = 0
counter_even = 0
cumulative = 0
largest_number = 0

while integer > 0:
    cumulative = cumulative + integer
    if cumulative > 0:
        print("Cumulative total: ", cumulative)
    if integer % 2 == 0:
        counter_even += 1
    elif integer % 2 != 0:
        counter_odd += 1
    if integer > largest_number:
        largest_number = integer
    integer = int(input("Enter an integer: "))
if (integer <= 0 and cumulative > 0):
    print("Largest number: " , largest_number)
    print( "Count of even numbers: " , counter_even)
    print("Count of odd numbers: " , counter_odd)


