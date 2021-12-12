def reverse_string(original_string):

    new_string = ""

    
    for i in range(len(original_string)):  
        new_string += original_string[len(original_string) - 1 - i]
    print (f"\nOriginal Word: {original_string} \nNew Word: {new_string}\n")

    return new_string
    
print("\nWelcome! This is a simple console app that reverses strings.")
user_input = input("Please enter a string and I will show you the reverse: ")

reverse_string(user_input)

# Start by creating an empty string. 
    # This will hold the value of the letters of the word 
    # you're reversing while you loop through them.

# The first line of the for loop establishes the beginning and end point 
    # of the loop. Because it's set at the length of the string, it will loop
    # from the beginning to the end of the string. While the string length is 
    # not the same as the index of the last letter, this works because the end 
    # point of a range is not inclusive. Using the len method is more dynamic 
    # but this can also be rewritten as follows for a 5 letter word like 'water' 
        # 'for i in range(0,5):' or 'for i in range(5):'
    
# The body of the for loop changes the value of the empty new_string. With each
    # iteration, it adds a letter from the end of original string to the new string. 
                    # *original_string[len(original_string) - 1]* 
    # establishes the index of the last letter of the original string. Subtracting i 
    # from this causes the value to change with each loop. At the 1st iteration, i is 0 
    # so the letter at the last index is added to the new string. At the 2nd iteration, 
    # i is 1 so instead of subtracting 1 from the length you subtract 2 and the second
    # to last letter is added to new_string. This continues until the loop is complete. 
    # Without the i, the loop would retrieve the last letter of the original string each time.
