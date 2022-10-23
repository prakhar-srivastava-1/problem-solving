class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])

        # if r, c are invalid dimensions
        if m * n != r * c: return mat

        row_wise = []
        for i in range(m):
            row_wise = row_wise + mat[i]
        
        new_mat = []
        for i in range(r):
            new_mat.append(row_wise[i*c:(i+1)*c])
                   
        return new_mat


