user_input = raw_input("Your haos string: ")
    
# for correct comparations
user_input_lower = user_input.lower()

# flag for ontime string cat
is_asc = False

# contain all asc strings
asc_array = []
    
# start point
prev_letter = user_input_lower[0]
prev_letter_index = 0

for i in range(0, len(user_input_lower) - 1):
    if user_input_lower[i] <= user_input_lower[i + 1]:
        is_asc = True
    else:
        is_asc = False
        asc_array.append( user_input[prev_letter_index:i+1] )
        prev_letter = user_input_lower[i + 1]
        prev_letter_index = i + 1
    
print "Result: " + max(asc_array, key=len)
