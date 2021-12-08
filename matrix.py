import unittest
class Matrix:
    def __init__(self, matrix):
        self.m = matrix

    def show(self):
        return self.m

    def __add__(self, other):
        if(len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0])):
            sumM = []
            for i in range(0, len(self.m)):
                sumR = [self.m[i][j] + other.m[i][j] for j in range(len(self.m[0]))]
                sumM.append(sumR)
            return sumM
        else:
            return "The order should be same for addition"


    def __sub__(self, other):
        if(len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0])):
            subM = []
            for i in range(0, len(self.m)):
                subR = [self.m[i][j] - other.m[i][j] for j in range(len(self.m[0]))]
                subM.append(subR)
            return subM
        else:
            return "The order should be same for subtraction"

    def __mul__(self, other):
        if(len(self.m[0]) == len(other.m)):
            mulM = Matrix([])
            mulM.m = [[0 for i in range(len(other.m[0]))] for j in range(len(self.m))]
            for i in range(len(self.m)):
                for j in range(len(other.m[0])):
                    for k in range(len(other.m)):
                        mulM.m[i][j] += self.m[i][k] * other.m[k][j]
            return mulM
        else:
            return "Can not multiply matrices with these order"
    
    def det(self):
        if len(self.m) == len(self.m[0]):
            temp = [0] * len(self.m)
            total = 1
            x = 1
            if(len(self.m) == 2):
                x = self.m[0][0] * self.m[1][1] - self.m[0][1]*self.m[1][0]
                return x
            else:
                for i in range(len(self.m)):
                    index = i
                    while (self.m[index][i] == 0 and index < len(self.m)):
                        index += 1
                    if (index == len(self.m)):
                        continue
                    if (index != i):
                        for j in range(len(self.m)):
                            self.m[index][j], self.m[i][j] = self.m[i][j], self.m[index][j]
                        x = x * int(pow(-1, index - i))
                    for j in range(len(self.m)):
                        temp[j] = self.m[i][j]
                    for j in range(i + 1, len(self.m)):
                        n1 = temp[i]
                        n2 = self.m[j][i]
                        for k in range(len(self.m)):
                            self.m[j][k] = (n1 * self.m[j][k]) - (n2 * temp[k])
                        total = total * n1
                for i in range(len(self.m)):
                    x = x * self.m[i][i]
                return int(x / total)
        else:
            return "Determinant is only possible for square matrices"

    def __pow__(self, x):
        if(len(self.m) == len(self.m[0])):
            exp = Matrix([])
            exp.m = self.m
            for k in range(x-1):
                exp = exp * self
            return exp.m
        else:
            return "Exponentiation is only possible for square matrix "

class Test(unittest.TestCase):
    def test_add(self):
        p1 = Matrix([[2, 3, 6], [4, 5, 8]])
        p2 = Matrix([[2, 3, 7], [4, 5, 7]])
        add = p1+p2
        self.assertEqual(add, [[4,6,13], [8, 10, 15]])
    def test_sub(self):
        p1 = Matrix([[7, 8, 9], [10, 11, 12]])
        p2 = Matrix([[1, 2, 3], [4, 5, 6]])
        sub = p1-p2
        self.assertEqual(sub, [[6, 6, 6], [6, 6, 6]])
    def test_mul(self):
        p1 = Matrix([[2, 4], [6, 8]])
        p2 = Matrix([[1, 3], [5, 7]])
        multi = p1*p2
        self.assertEqual(multi.show(), [[22, 34], [46, 74]])
    def test_det(self):
        p1 = Matrix([[1, 2, 3], [5, 4, 7], [2, 3, 2]])
        deter = p1.det()
        self.assertEqual(deter, 16)
    def test_pow(self):
        p1 = Matrix([[1, 2, 3], [5, 6, 7], [11, 12, 13]])
        power = p1**3
        self.assertEqual(power, [[910, 1060, 1210], [2390, 2780, 3170], [4610, 5360, 6110]])

if __name__ == "__main__":
    unittest.main()


