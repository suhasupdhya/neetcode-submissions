class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2

            total = 0
            for pile in piles:
                total += (pile + mid - 1) // mid   # Ceiling division

            if total <= h:
                ans = mid          # This speed works
                r = mid - 1        # Try a smaller speed
            else:
                l = mid + 1        # Too slow, increase speed

        return ans