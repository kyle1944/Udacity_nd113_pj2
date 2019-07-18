import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if len(self.g) == 1 :
            det = 1/self.g[0][0]
        else :
            det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return det
        

        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace_result = 0
        for i in range(self.h) : trace_result += self.g[i][i]
        return trace_result

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse_matrix=[]
        if len(self.g) == 1 :
            inverse_matrix = [[1/self.g[0][0]]]
        else :
            det = self.determinant()            
            inverse_matrix = [
                [self.g[1][1]/det, -self.g[0][1]/det],
                [-self.g[1][0]/det, self.g[0][0]/det]
            ]
        
        return Matrix(inverse_matrix)

            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose_result = []
        for j in range(len(self.g[0])):
            tmp = []
            for i in range(len(self.g)):
                tmp.append(self.g[i][j])
            transpose_result.append(tmp)
        return Matrix(transpose_result)
            

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        add_result = []
        for i in range(self.h):
            tmp = []
            for j in range(self.w):
                tmp.append(self.g[i][j] + other.g[i][j])
            add_result.append(tmp)
        return Matrix(add_result)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_result = []
        for i in range(self.h):
            tmp = []
            for j in range(self.w):
                tmp.append(-self.g[i][j])
            neg_result.append(tmp)
        return Matrix(neg_result)
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        sub_result = []
        for i in range(self.h):
            tmp = []
            for j in range(self.w):
                tmp.append(self.g[i][j] - other.g[i][j])
            sub_result.append(tmp)
        return Matrix(sub_result)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        mul_result = []
        for rowN in range(self.h):
            res_tmp = []
            for colN in range(other.w):
                sum_tmp = 0
                for eleN in range(self.w) :
                    sum_tmp += self.g[rowN][eleN]*other.g[eleN][colN]
                res_tmp.append(sum_tmp)
            mul_result.append(res_tmp)
        return Matrix(mul_result)
                
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmul_result = []
            for i in range(self.h):
                tmp = []
                for j in range(self.w):
                    tmp.append(other*self.g[i][j])
                rmul_result.append(tmp)
            return Matrix(rmul_result)
            