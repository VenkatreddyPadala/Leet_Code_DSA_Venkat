class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Main logic is adding [0] to the start and end of the row so that its easy to add and put it in that slot.
        res = [[1]]
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
        
        