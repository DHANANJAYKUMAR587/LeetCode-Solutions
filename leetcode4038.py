#leetcode 4038
# LeetCode 4038 - Count Integers Appearing in a Single Block
# Difficulty: Easy
#
# Problem:
# Count the distinct integers whose occurrences appear
# in only one contiguous block in the array.
#
# Example:
# nums = [1, 2, 2, 1]
# Output: 1
#
# Approach:
# Find the positions where each number appears.
# If its occurrences form one continuous block, count it.
nums = [7, 42, 13, 99, 24, 68, 5, 31, 87, 16, 73, 2, 55, 91, 38, 64, 11, 100, 27, 49, 83, 6, 35, 72, 19]
count=0
a=sorted(list(set(nums)))
for i in a:
    ans=[]
    for idx,val in enumerate(nums):
        if val==i:
            ans.append(idx)
    if len(ans)==1:
        count+=1
    total=[]
    for i in range(len(ans)-1):
        total.append(ans[i+1]-ans[i])
    if sum(set(total))==1:
        count+=1
print(count)