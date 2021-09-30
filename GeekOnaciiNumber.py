# def Geeko(a,b,c,n):
#     sum = 0
#     if n==3:
#         return c
#     else:
#         sum = a+b+c
#     return(Geeko(b,c,sum,n-1))


# t = int(input('Enter the number of test cases: '))
# for i in range(t):
#     arr = [int(t) for t in input().strip().split()]
#     print(arr)
#     a,b,c,n = arr[0],arr[1],arr[2],arr[3]
#     print(Geeko(a,b,c,n))

def geeko(arr,n):
    for i in range(3,n):
        sum = arr[i-1]+arr[i-2]+arr[i-3]
        arr.append(sum)
    return(arr[n-1])

if __name__ =='__main__':
    t = int(input())
    for i in range (t):
        ax = int(input('Enter the numbers and n: ').split())
        arr = ax[:-1]
    n =ax[3]
    
    print(geeko(arr,n))