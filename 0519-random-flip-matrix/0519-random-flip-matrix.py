import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total_cells = m * n
        self.used_cells = set()

    def flip(self) -> List[int]:
        # Generate a random index until an unused one is found
        while True:
            random_index = random.randint(0, self.total_cells - 1)
            i, j = divmod(random_index, self.n)
            if (i, j) not in self.used_cells:
                self.used_cells.add((i, j))
                return [i, j]

    def reset(self) -> None:
        # Reset the set of used cells
        self.used_cells = set()

# Example usage:
solution = Solution(3, 1)
print(solution.flip())  # Output: [1, 0]
print(solution.flip())  # Output: [2, 0]
print(solution.flip())  # Output: [0, 0]
solution.reset()
print(solution.flip())  # Output: [2, 0]
