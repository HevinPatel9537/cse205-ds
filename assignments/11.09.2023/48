class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])

        first,last = 0,rows-1
        
        while(first<last):
            matrix[first],matrix[last] = matrix[last],matrix[first]
            first +=1
            last -=1
        
        for i in range(0,rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]