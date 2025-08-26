# c1 Maxsubset sum no adjacent


# list1 = [75, 105, 120, 75, 90, 135]  # 135 + 120 + 75 = 330


# # take the list1 go at the highest number's index then take out its +1 ,-1 and itself
# # del , index , in
# # order sort , in , index , del


# def maxSubset(list):
#     sum = 0
#     sortedList = sorted(list, reverse=True)
#     for i in sortedList:
#         if i in list:
#             sum += i
#             deleting = list.index(i)
            
              
            
#     print(sum)


# maxSubset(list1)


# keep doing this till you have no more elements




''' Struggled with syntax for conditional logic '''
















list1 = [75, 105, 120, 75, 90, 135]  # Expected: 135 + 120 + 75 = 330

# def maxSubset(arr):
#     if not arr:
#         return 0
    
#     # Create a copy to avoid modifying the original
#     remaining = arr.copy()
#     total_sum = 0
    
#     while remaining:
#         # Find the maximum value and its index
#         max_val = max(remaining)
#         max_idx = remaining.index(max_val)
        
#         # Add to sum
#         total_sum += max_val
#         print(f"Selected: {max_val} at index {max_idx}")
        
#         # Remove the selected element and its adjacent elements
#         indices_to_remove = []
        
#         # Add current index
#         indices_to_remove.append(max_idx)
        
#         # Add adjacent indices if they exist
#         if max_idx > 0:  # Left adjacent
#             indices_to_remove.append(max_idx - 1)
#         if max_idx < len(remaining) - 1:  # Right adjacent
#             indices_to_remove.append(max_idx + 1)
        
#         # Sort in descending order to remove from right to left (avoids index shifting)
#         indices_to_remove.sort(reverse=True)
        
#         # Remove elements
#         for idx in indices_to_remove:
#             print(f"Removing element at index {idx}: {remaining[idx]}")
#             remaining.pop(idx)
        
#         print(f"Remaining list: {remaining}")
#         print("---")
    
#     return total_sum

# # Test the function
# result = maxSubset(list1)
# print(f"Maximum subset sum: {result}")

print("\n" + "="*50)
print("Alternative Dynamic Programming Solution (Optimal):")

def maxSubsetDP(arr):
    """
    Dynamic Programming solution - guaranteed optimal result
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    # dp[i] represents max sum up to index i
    dp = [0] * len(arr)
    dp[0] = max(0, arr[0])  # Can choose not to include if negative
    dp[1] = max(dp[0], arr[1], dp[0])  # Max of: prev_max, current, or prev_max
    
    for i in range(2, len(arr)):
        # Either include current + best sum up to i-2, or exclude current (take i-1)
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[-1]

dp_result = maxSubsetDP(list1)
print(f"DP Maximum subset sum: {dp_result}")
