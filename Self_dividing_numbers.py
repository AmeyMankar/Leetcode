class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for i in range(left, right+1):
        	if i in range(1,10):
        		answer.append(i)
        	if i % 10 != 0:
        		print(len(str(i)))
        		print(str(i)[0])
        		print(str(i)[1])




s = Solution()
s.selfDividingNumbers(1,22)