# HEMIT PATEL
# 781159

# python random lib lets us get a random int through the fucntion randint
# i only import the randint function
# it isnt in python by default hence the need to import it!

from random import randint

def generate_random_arr(amount_numbers: int):
    num_arr = []

    # _ in use because we do not need the counter variable
    # here we get the different random numbers that will be used
    # a new random number will be added until the amount of numbers (in range)
    # is sastified (amount of iterations)

    for _ in range(amount_numbers):
        num = randint(1,200)

        num_arr.append(num)
    
    return num_arr


def computation(target: int, num_arr):
    # flag set to see if an answer was found, this way we can output something if not able to find nything
    found_answer = False

    for addend_1_idx in range(len(num_arr)):
        # for each idx we will run through all other indexs other than the ones
        # already iterated through creating a range from addend_1_idx to the end of the arr (length)
        # for example, if addend_1_idx == 3 that means this nested loop will iterate from 4 - LENGTH,
        # skipping 1,2,3
        
        for addend_2_idx in range(addend_1_idx, len(num_arr)):
            # checking if both index's numbers add up to target
            if (num_arr[addend_1_idx] + num_arr[addend_2_idx] == target):
                # if so break as the question says to return it (break in other words)
                # set flag to true because we found the answer
                
                found_answer = True
                
                # return will break the for loop autometically as per python regulations
                return [addend_1_idx, addend_2_idx]
                
        
        

    # if found answer event never happend, we can just print out not possible
    # BONUS SOLUTION

    if (found_answer == False):
        return "Not possible"

amount_numbers = int(input("Enter the amount of numbers:"))
target = int(input("Enter target amount:"))
num_arr = generate_random_arr(amount_numbers)

print(computation(target, num_arr))
