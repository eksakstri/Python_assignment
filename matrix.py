import unittest
class Matrix:
    def __init__(self, matrix):
        self.A = matrix

    def show(self):
        return self.A

    def __add__(self, B):
        if(len(self.A) == len(B.A) and len(self.A[0]) == len(B.A[0])):
            sumM = []
            for i in range(0, len(self.A)):
                sumR = [self.A[i][j] + B.A[i][j] for j in range(len(self.A[0]))]
                sumM.append(sumR)
            return sumM
        else:
            return "The order should be same for addition"


    def __sub__(self, B):
        if(len(self.A) == len(B.A) and len(self.A[0]) == len(B.A[0])):
            subM = []
            for i in range(0, len(self.A)):
                subR = [self.A[i][j] - B.A[i][j] for j in range(len(self.A[0]))]
                subM.append(subR)
            return subM
        else:
            return "The order should be same for subtraction"

    def __mul__(self, B):
        if(len(self.A[0]) == len(B.A)):
            mulM = Matrix([])
            mulM.A = [[0 for i in range(len(B.A[0]))] for j in range(len(self.A))]
            for i in range(len(self.A)):
                for j in range(len(B.A[0])):
                    for k in range(len(B.A)):
                        mulM.A[i][j] += self.A[i][k] * B.A[k][j]
            return mulM
        else:
            return "Can not multiply matrices with these order"
    
    def det(self):
        if len(self.A) == len(self.A[0]):
            temp = [0] * len(self.A)
            T = 1
            x = 1
            if(len(self.A) == 2):
                x = ((self.A[0][0] * self.A[1][1]) - (self.A[0][1]*self.A[1][0]))
                return x
            else:
                for i in range(len(self.A)):
                    a = i
                    while (self.A[a][i] == 0 and a < len(self.A)):
                        a += 1
                    if (a == len(self.A)):
                        continue
                    if (a != i):
                        for j in range(len(self.A)):
                            self.A[a][j], self.A[i][j] = self.A[i][j], self.A[a][j]
                        x = x * int(pow(-1, a - i))
                    for j in range(len(self.A)):
                        temp[j] = self.A[i][j]
                    for j in range(i + 1, len(self.A)):
                        n1 = temp[i]
                        n2 = self.A[j][i]
                        for k in range(len(self.A)):
                            self.A[j][k] = (n1 * self.A[j][k]) - (n2 * temp[k])
                        T = T * n1
                for i in range(len(self.A)):
                    x = x * self.A[i][i]
                return int(x / T)
        else:
            return "Determinant is only possible for square matrices"

    def __pow__(self, x):
        if(len(self.A) == len(self.A[0])):
            exp = Matrix([])
            exp.A = self.A
            for k in range(x-1):
                exp = exp * self
            return exp.A
        else:
            return "Exponentiation is only possible for square matrix "

class Test(unittest.TestCase):
    def test_add(self):
        m1 = Matrix([[2, 3, 6], [4, 5, 8]])
        m2 = Matrix([[2, 3, 7], [4, 5, 7]])
        add = m1+m2
        self.assertEqual(add, [[4,6,13], [8, 10, 15]])
    def test_sub(self):
        m1 = Matrix([[7, 8, 9], [10, 11, 12]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        sub = m1-m2
        self.assertEqual(sub, [[6, 6, 6], [6, 6, 6]])
    def test_mul(self):
        m1 = Matrix([[2, 4], [6, 8]])
        m2 = Matrix([[1, 3], [5, 7]])
        mul = m1*m2
        self.assertEqual(mul.show(), [[22, 34], [46, 74]])
    def test_det(self):
        m1 = Matrix([[1, 2, 3], [5, 4, 7], [2, 3, 2]])
        det = m1.det()
        self.assertEqual(det, 16)
    def test_pow(self):
        m1 = Matrix([[1, 2, 3], [5, 6, 7], [11, 12, 13]])
        pow = m1**3
        self.assertEqual(pow, [[910, 1060, 1210], [2390, 2780, 3170], [4610, 5360, 6110]])

if __name__ == "__main__":
    unittest.main()


