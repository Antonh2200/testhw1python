num_int = int(input("Input a number: "))    # Do not change this line

num_1 = 0
num_2 = 0

while num_int > 0:
    num_1 = num_int
    if num_1 > num_2:
        num_2 = num_1
    else:
        num_int = int(input("Input a number: "))


print("The maximum is", num_2)    # Do not change this line
