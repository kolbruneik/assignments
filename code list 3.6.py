# Newton's method to calculate square root

#get three inputs from the user( two int, 1 float)
#note not robust on bad input
number_str=input("Find the square root of integer: ")
number_int=int(number_str)
guess_str =int("Initial guess: ")
guess_float=float(guess_str)
tolerance_float = float(input("what tolerance: "))

orginal_guess_float=guess_float
count_int=0
previous_float=0

while abs(previous_float - guess_float)> tolerance_float:
    previous_float=guess_float
    quotient_float=guess_float
    guess_float=(quotient_float + guess_float)/2
    count_int = count_int + 1
print("square root of", number_int, "is:", guess_float)
print("Took ", count_int, "repst to get tolerance: ", tolerance_float)
print("starting from a guess of: ", original_guess_float)
