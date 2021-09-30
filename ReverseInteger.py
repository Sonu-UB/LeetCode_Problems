# def reverse(x):
#     new_num = 0
#     input_num = abs(x)
#     while input_num>0:
#         new_num = new_num*10 + input_num/10
#         input_num = input_num//10
#     if x<0:
#         return 0 if -new_num<-(2**31)-1 else -new_num

#     return new_num if new_num < 2**31 else 0

# x = 123
# print(reverse(x))

def reverse(x):
    int_max = 0x7FFFFFFF
    int_min = ~int_max
    if x == int_min:
        return 0

    rev = 0
    sign =1 if x>=0 else -1
    x = abs(x)
    while x!=0:
        digit = x%10
        if rev >(int_max-digit)//10:
            return 0 
        rev = rev*10 +digit
        x = x//10
    return rev*sign


x = -124
print(reverse(x))