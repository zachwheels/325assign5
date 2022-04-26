def max_independent_set(nums):
    grid = [[0 for x in range(len(nums))] for x in range(len(nums))]
    elementGrid = [[0 for x in range(len(nums))] for x in range(len(nums))]
    maxSum = []
    if(len(nums) < 1):
        return maxSum
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            grid[i][j] = nums[i]
            newArray = []
            newArray.append(nums[i])
            elementGrid[i][j] = newArray

    for i in range(len(nums)):
        for j in range(len(nums)):
            if(j < i + 2):
                if(i > 0 and j == len(nums) - 1):
                    if(grid[i-1][j] > grid[i][j]):
                        grid[i][j] = grid[i-1][j]
                else:
                    continue
            elif(grid[i][j - 1] > nums[j] + grid[i][j - 2]):
                grid[i][j] = grid[i][j - 1]
                elementGrid[i][j] = elementGrid[i][j - 1]
            else:
                grid[i][j] = nums[j] + grid[i][j - 2]
                newArray = []
                newArray.append(nums[j])
                newArray.append(elementGrid[i][j - 2])
                elementGrid[i][j] = newArray
                if(grid[i][j - 1] > grid[i][j]):
                    grid[i][j] = grid[i][j - 1]
            if(i > 0 and j == len(nums) - 1):
                if(grid[i-1][j] > grid[i][j]):
                    grid[i][j] = grid[i-1][j]

    for i in range(len(nums) - 1, -1, -1):
        if(grid[i - 1][len(nums) - 1] == grid[i][len(nums) - 1]):
            continue
        else:
            break
    
    def unpack(arr1, arr2):
        for i in range(len(arr1)):
            if(type(arr1[i]) == int):
                arr2.append(arr1[i])
            else:
                (unpack(arr1[i], arr2))
        return(arr2)
            
    newArray = []
    gridArray = elementGrid[i][len(nums) - 1]

    unpacked = unpack(gridArray, newArray)
    if(sum(unpacked) < 0):
        return []
    else:
        return unpacked
        
nums = [-9, 4, -5, 0, -4, 11, 6]
print(max_independent_set(nums))
