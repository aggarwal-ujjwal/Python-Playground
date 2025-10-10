user_input = input("Enter TO-DO: ")
#use input argument to print

# first think of naive solution and then optimize it
# don't start right away and first discuss high level solution
# Don't go silent, always keep communicating with the interview


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

