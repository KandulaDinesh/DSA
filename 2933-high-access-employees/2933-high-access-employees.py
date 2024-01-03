from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # Create a defaultdict to store access times for each employee.
        eDict = defaultdict(list)

        # Populate the defaultdict with employee names and corresponding access times.
        for employee, time in access_times:
            eDict[employee].append(int(time))

        # Initialize the result list to store high-access employees.
        result = []

        # Iterate through the defaultdict to check for high-access employees.
        for employee, times in eDict.items():
            # Sort the access times in ascending order.
            times.sort()
            n = len(times)
            
            # Iterate through the sorted access times to check for three or more accesses within a one-hour period.
            for i in range(n - 2):
                if times[i + 2] - times[i] < 100:
                    # If three or more accesses are found within a one-hour period, add the employee to the result.
                    result.append(employee)
                    break

        return result
