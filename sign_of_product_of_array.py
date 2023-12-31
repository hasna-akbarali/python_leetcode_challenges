def arraySign(self, nums):
        """
        There is a function signFunc(x) that returns:
        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.
        You are given an integer array nums. 
        Let product be the product of all values in the array nums.

        Example 1:

        Input: nums = [-1,-2,-3,-4,3,2,1]
        Output: 1
        Explanation: The product of all values in the array is 144, and signFunc(144) = 1
        
        """

        prod = 1
        for i in nums:
            if i<0:
                prod*=-1
            elif i==0:
                prod*=0
        return prod
