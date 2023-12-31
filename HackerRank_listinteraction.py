if __name__ == '__main__':
    N = int(input())
    
    commands = []
    for _ in range(N):
        commands.append(input().split())

    output = []
    for command in commands:
        if command[0]=='append':
            output.append(int(command[1]))
        elif command[0]=='insert':
            output.insert(int(command[1]),int(command[2]))
        elif command[0]=='print':
            print(output)
        elif command[0]=='remove':
            output.remove(int(command[1]))
        elif command[0]=='sort':
            output.sort()
        elif command[0]=='pop':
            if len(command)==1:
                output.pop()
            else:
                output.pop(command[1])
        elif command[0]=='reverse':
            output.reverse()
