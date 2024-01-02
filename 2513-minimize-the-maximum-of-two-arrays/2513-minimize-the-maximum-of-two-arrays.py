from math import gcd

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r, ans = 1, 10**15, 10**15
        d1, d2, cnt1, cnt2 = divisor1, divisor2, uniqueCnt1, uniqueCnt2

        g = gcd(d1, d2)
        lcm = (d1 * d2) // g

        while l <= r:
            mid = (l + r) // 2

            common = mid // lcm
            c1 = (mid // d1) - common
            c2 = (mid // d2) - common

            z1, z2 = cnt1 - min(cnt1, c2), cnt2 - min(cnt2, c1)
            avail = mid - (c1 + c2 + common)

            if z1 + z2 <= avail:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


