import sys
N = int(sys.stdin.readline())
stack = []


for _ in range(N):
    a = sys.stdin.readline().strip()

    if a.startswith('push'): #push 구현
        stack.append(a.split()[-1])

    elif a == 'top': #top 구현
        if stack == []:
            print(-1)
        else:
            print(stack[-1])

    elif a == 'pop': #pop 구현
        if stack == []:
            print(-1)
        else:
            pop = stack.pop()
            print(pop)

    elif a == 'size': #size 구현
        print(len(stack))

    elif a == 'empty': #empty 구현
        if stack == []:
            print(1)
        else:
            print(0)

    

