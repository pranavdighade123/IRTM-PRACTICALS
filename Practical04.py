def count_characters(s):
    upper, lower, number, special = 0, 0, 0, 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            number += 1
        else:
            special += 1

    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', number)
    print('Special characters:', special)

# Driver Code
input_str = "#GeeKs01fOr@gEEks07"
count_characters(input_str)
