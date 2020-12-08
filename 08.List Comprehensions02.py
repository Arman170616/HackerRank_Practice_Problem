if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result =[]
    result=[[i,j,k]  for i in range(x+1) for i in range(y+1) for i in range(z+1) if i+j+k !=n]
    print(result)
