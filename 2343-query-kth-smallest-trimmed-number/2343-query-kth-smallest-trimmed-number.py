from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = [""] * len(queries)
        trimmedToTheLast = {}
        
        for i, (k, trim) in enumerate(queries):
            # Check if the trimmed numbers for the current trim value are already calculated.
            if trim not in trimmedToTheLast.keys():
                # Create a list of tuples with the trimmed number and its original index.
                trimmed_nums_with_indices = []
                for j, num in enumerate(nums):
                    trimmed_nums_with_indices.append((num[-trim:], j))

                # Sort the list of tuples and store it in the trimmedToTheLast dictionary.
                trimmedToTheLast[trim] = sorted(trimmed_nums_with_indices)

            # Assign the original index of the kth smallest trimmed number to the answer list.
            answer[i] = trimmedToTheLast[trim][k - 1][1]

        return answer


