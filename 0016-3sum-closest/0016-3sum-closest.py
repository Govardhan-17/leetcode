class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Initialize the closest sum to a large value (or any valid initial sum)
        closest_sum = float('inf')
        
        # Step 3: Iterate through the array
        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Two pointers
            
            # Step 4: Use two pointers to find the closest sum
            while left < right:
                # Calculate current sum
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is exactly equal to the target, return it
                if current_sum == target:
                    return current_sum
                
                # If the current sum is closer to the target, update the closest sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers to get a closer sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        # Step 5: Return the closest sum found
        return closest_sum

# Example Usage:
sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(sol.threeSumClosest([0, 0, 0], 1))      # Output: 0
