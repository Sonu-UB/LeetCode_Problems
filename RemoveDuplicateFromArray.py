def removeDup(nums):
    lenght = 0
    if len(nums)==0:
        return lenght
    for i in range(1,len(nums)):
        if nums[lenght]<nums[i]:
            lenght+=1
            nums[lenght]=nums[i]
        
    return lenght+1