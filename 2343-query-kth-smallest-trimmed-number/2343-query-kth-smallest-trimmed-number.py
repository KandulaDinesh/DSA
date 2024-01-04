from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []

        for k, trim in queries:
            # Step 1: Trim each number to its rightmost 'trim' digits.
            trimmed_nums = [num[-trim:] for num in nums]

            # Step 2: Create a list of tuples with the trimmed number and its original index.
            nums_with_index = [(int(trimmed_num), i) for i, trimmed_num in enumerate(trimmed_nums)]

            # Step 3: Sort the list of tuples based on the trimmed number.
            nums_with_index.sort()

            # Step 4: Append the original index of the kth smallest trimmed number to the answer list.
            answer.append(nums_with_index[k - 1][1])

        return answer

# Example usage:
solution_instance = Solution()
result = solution_instance.smallestTrimmedNumbers(["24", "37", "96", "04"], [[2, 1], [2, 2]])
print(result)  # Expected Output: [3, 0]
