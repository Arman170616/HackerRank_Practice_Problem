lst = []
n = int(input())
for i in range(n):
    val = input().split()
    if val[0]=='insert':
        lst.insert(int(val[1]),int(val[2]))    
    elif val[0]=='print':
        print(lst)
    elif val[0]=='remove':
        lst.remove(int(val[1]))
    elif val[0]=='append':
        lst.append(int(val[1]))
    elif val[0]=='sort':
        lst.sort()
    elif val[0]=='pop':
        lst.pop()
    else:
        lst.reverse()
