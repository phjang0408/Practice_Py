li = []
wait = True
while True:
    cmd = int(input())
    if cmd == 1:
        if wait == False:
            print("Waiting End")
            continue
        else:
            p = input()
            li.append(p)
    elif cmd == 2:
        print(li[0])
        li.remove(li[0])
    elif cmd == 3:
        wait = False
    elif cmd == 4:
        print(li)
    elif cmd == 5:
        break