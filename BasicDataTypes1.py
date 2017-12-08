if __name__ == '__main__':
    N = int(raw_input())
    L=[];

for i in range(0,N):
    command=raw_input().split();
    if command[0] == "insert":
        L.insert(int(command[1]),int(command[2]))
    elif command[0] == "append":
        L.append(int(command[1]))
    elif command[0] == "pop":
        L.pop();
    elif command[0] == "print":
        print L
    elif command[0] == "remove":
        L.remove(int(command[1]))
    elif command[0] == "sort":
        L.sort();
    else:
        L.reverse();
