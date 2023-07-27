

if __name__ == '__main__':
    N = int(input())
    
    commands = []
    for _ in range(N):
        commands.append(input().split())

    output = []
    for command in commands:
        if command[0]=='append':
            output.append(int(command[1]))
    
    print(output)