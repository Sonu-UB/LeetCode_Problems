# def matrixReshape(mat,r,c):
#     N, M = len(mat[0]),len(mat)
#     T = r*c
#     if N*M != T:
#         return mat

#     output = [[0 for _ in range (c)] for _ in range (r)]
#     k=0
#     for i in range(M):
#         for j in range(N):
#             output[k//c][k%c] = mat[i][j]
#             k+=1

#     return output  

# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     while low <= high:
#         mid = (high + low) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return True
#     return False  

# def searchMatrix(matrix , target):
#     reshaped = matrixReshape(matrix,)
#     isPresent = binary_search(reshaped,target)
#     return isPresent


# print(searchMatrix(matrix,target))

from typing import List


def searchMatrix(matrix: List[List[int]], target:int)-> bool:
        if len(matrix) == 0:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: row += 1
            elif matrix[row][col] > target: col -= 1
        
        return False

matrix =[1,3,5,7],[10,11,16,20],[23,30,34,60]
target = 13
print(searchMatrix(matrix, target))