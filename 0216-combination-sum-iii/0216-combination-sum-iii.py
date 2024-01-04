from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, current_combination):
            # Base case: If the current combination is valid, add it to the result.
            if target == 0 and len(current_combination) == k:
                result.append(current_combination[:])
                return

            # Explore all possible choices from the current start index.
            for i in range(start, 10):
                # Avoid using the same number more than once.
                if i in current_combination:
                    continue

                # Backtrack with the current choice.
                current_combination.append(i)
                backtrack(i + 1, target - i, current_combination)

                # Undo the choice for backtracking.
                current_combination.pop()

        result = []
        backtrack(1, n, [])
        return result
