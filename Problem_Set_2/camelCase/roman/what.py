def modify_string(preName):
    """
    Modifies a string by inserting spaces before each uppercase letter (except the first one).

    Parameters:
    preName (str): The input string to be modified.

    Returns:
    str: The modified string with spaces inserted before each uppercase letter (except the first one).
    """
    nameIndex = []
    nameIndex.append(preName[0].upper())
    for i, char in enumerate(preName[1:]):
        if char.isupper():
            if i > 0:
                nameIndex.append(" ")
        nameIndex.append(char)  
    print(nameIndex)
    return "".join(nameIndex)


name = input("Enter your name in cC:")
callFunction = modify_string(name)
print(callFunction)

#----------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

import re
def insert_spaces_regex(text):
    pattern = r"[a-z]+(?=[A-Z])"
    result = re.sub(pattern, r"/g ", text)
    return result[0].upper() + result[1:]
input_string = fijhHHFOjhphjfPHJP
output_string = insert_spaces_regex(input_string)
print(output_string)

"""
#----------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

def insert_spaces_loop(text):
    result = ""
    result += text[0].upper()
    for i in range(1, len(text)):
        char = text[i]
        if char.isupper() and i > 0 and text[i-1] != ' ':
            result += " "
        result += char
    return result

"""