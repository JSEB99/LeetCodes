def swap_case(s:str)->str:

    swapped_string= [letter.lower() if letter.isupper() else letter.upper() for letter in s]

    return "".join(swapped_string)

if __name__=='__main__':
    string = input()
    result = swap_case(string)
    print(result)