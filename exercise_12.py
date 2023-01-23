def shift_lower_remove_spaces(string_input):
    #lists
    low = [ ]
    upper = [ ]
    for char in string_input:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            low.append(char)

    output = ' '.join(low) + ' '.join(upper)
    return output
inp = input("Enter words: ")
print(shift_lower_remove_spaces(inp))