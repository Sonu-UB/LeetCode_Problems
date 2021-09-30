def intersect(nums1, nums2):
    d={}
    final=[]

    for i in nums1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        
    for i in nums2:
        if i in d:
            if d[i] > 1:
                d[i] -= 1
            else:
                del d[i]
            final.append(i)

    return final

n = [4,9,5]
m=[9,4,9,8,4]

print(intersect(n,m))