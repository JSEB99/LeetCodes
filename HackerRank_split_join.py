def split_and_join(line):

    string_splitted = line.split()

    return "-".join(string_splitted)

if __name__=='__main__':
    line = input()
    result = split_and_join(line)
    print(result)