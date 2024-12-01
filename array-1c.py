# HEMIT PATEL
# 781159

def get_first_last_occurance(nums: list, target: int):
    
    # find the first occurance (index method finds the first of the target occurance and returns the index pos)
    # we must turn target into str because the list holds the numbers in a list format

    start = nums.index(str(target))

    # initalize end var outside scope so it can be used globally 
    end = 0

    # here we check if there are any elements within the list
    # if not, no indexes were found w/ target
    # so no need to even continue with the rest of the program
    if start == -1:
        # return -1,-1 as that indicates nothing was found and will stop execution of this function
        return [-1, -1]

    # find the last occurance
    # the -1 within the range ensures that we start backwards (through counting backwards in the steps + starting at the end value (-1 represents that))
    
    for i in range(len(nums)-1, -1, -1):
        if int(nums[i]) == target:
            end = i
            break

# return this to give the start idx and end idx

    return [start, end]


# getting all of the inputs
nums = input().split()
target = int(input())

# run function 
print(get_first_last_occurance(nums, target))
