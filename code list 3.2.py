# Calculate the avarage of sum of consecutive integers in a given range.


limit_str = input(" Range is from 1 to you input: ")
limit_int = int(limit_str)

count_int= 1
sum_int = 0

while count_int <= limit_int:
    sum_int = sum_int + count_int
    count_int = count_int + 1

avarage_float = sum_int / (count_int - 1)

print( " Avarage of sum of integers from 1 to ", limit_int, "is", avarage_float)


