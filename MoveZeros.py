def moveZero(nums):
    pos = 0

    for i in range(len(nums)):
        num = nums[i]
        if num != 0:
            nums[pos],nums[i] = nums[i],nums[pos]
            pos +=1
            
