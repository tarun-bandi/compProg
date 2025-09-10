class Solution:
    def climbStairs(self, n: int) -> int:
        """
        i [0, n]

        Order: term i requires
                term i - 1, term i - 2
                0 before n
        """

            

        # count_ways_values = [None] * (n + 1)

        two_before = 1
        one_before = 1
        for i in range(2, n + 1):
            curr_result = two_before + one_before
            two_before = one_before
            one_before = curr_result
        return one_before

        @cache
        def count_ways(i: int):
            if i == 0:
                return 1
            if i == 1:
                return 1

            return count_ways(i - 1) + count_ways(i - 2)
        
        return count_ways(n)