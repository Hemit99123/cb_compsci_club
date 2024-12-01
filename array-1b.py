# HEMIT PATEL
# 781159

def generate_pascal_triangle(num_rows: int):
    # initialize the first row which is simply 1 (top of the pascal triangle)
    prev_row = [1]

    # list to store Pascal's Triangle rows
    # the prev row is added which will just add [1] to that pascal row to account for the first row, this way i dont repeat myself
    pascal_row = [prev_row]

    for _ in range(num_rows - 1):
        # the first element in each row is one, so we start off w that

        row = [1] 
        
        # generate the values for the inner elements of the row

        for idx in range(len(prev_row) - 1):

            # the pascal triangle is formed by adding the prev lists element with the next and putting that sum in a new list

            row.append(prev_row[idx] + prev_row[idx + 1])
        
        # now that all the new numbers from the computation are added, we add 1 which will be added to the END of the row
        # all rows have this attribute
        row.append(1)
        
        # add the row to the triangle list
        pascal_row.append(row)
        
        # update the previous row to the current row as computation for the rows are based on the older ones
        prev_row = row

# once computation is over, return the pascal row back to the user who called the function

    return pascal_row


num_rows = int(input("Enter the number of rows:"))
print(generate_pascal_triangle(num_rows))
