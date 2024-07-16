# Time complexity = O(3^(n+m))
# Space Complexity = O(n+m)
def edit_distance(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)

    def helper(index1, index2):        
        # Base Case
        if index2 > len_2 - 1:
            return len_1 - index1
        
        if index1 > len_1 - 1:
            return len_2 - index2
        
        # Recursive
        # Equal
        if text1[index1] == text2[index2]:
            return helper(index1+1, index2+1)
        
        # Not Equal
        insert = 1 + helper(index1, index2+1)
        delete = 1 + helper(index1, index2)
        replace = 1 + helper(index1+1, index2+1)

        return min(insert, delete, replace)
    
    return helper(0,0)

# Space Complexity = O(n * m) + O(n + m) = O(n * m)
# Time Complexity = O(n * m)
def edit_distance_memoization(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)
    dp = [[-1] * len_1 for _  in range(len_2)]

    def helper(index1, index2):        
        # Base Case
        if index2 > len_2 - 1:
            return len_1 - index1
        
        if index1 > len_1 - 1:
            return len_2 - index2
        
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        
        # Recursive
        # Equal
        if text1[index1] == text2[index2]:
            dp[index1][index2] = helper(index1+1, index2+1)
        
        # Not Equal
        insert = 1 + helper(index1, index2+1)
        delete = 1 + helper(index1, index2)
        replace = 1 + helper(index1+1, index2+1)

        dp[index1][index2] = min(insert, delete, replace)
        return dp[index1][index2]
    
    return helper(0,0)