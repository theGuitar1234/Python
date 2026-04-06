import math
from typing import override

class Vectors :
    @staticmethod
    def addition(vector1, vector2) :
        result = []
        if len(vector1) != len(vector2) :
            raise ValueError("2 vectors needs to be the same size")
        for i in range(len(vector1)) :
            result.append(vector1[i]+vector2[i])
        
        return result
    
    @staticmethod
    def scalar_multiplication(vector1, vector2) :
        z = 0
        result = []
        if len(vector1) != len(vector2) :
            raise ValueError("2 vectors needs to be the same size")
        for i in range(len(vector1)) :
            result.append(vector1[i]*vector2[i])
        for i in result :
            z += i
        
        return z
    
    @staticmethod
    def multiplication(vector, x) :
        result = []
        for i in vector :
            result.append(i*x)
        
        return result
    
    def length(self, vector) :
        z = 0
        for i in vector :
            z += math.pow(i, 2)
     
        return math.sqrt(z)
        

    def rube(self, vector) :
        if len(vector) != 2 :
            raise ValueError("The Vector size must be 2")

        if vector[0] and vector[1] > 0 :
            return f"{vector} is in the 1st rube"

        elif vector[0] < 0 and vector[1] > 0 :
            return f"{vector} is in the 2nd rube"

        elif vector[0] < 0 and vector[1] < 0 :
            return f"{vector} is in the 3rd rube"

        elif vector[0] > 0 and vector[1] < 0 :
            return f"{vector} is in the 4th rube"

class Matrices(Vectors) :
    @override
    @staticmethod
    def addition(matrix1, matrix2) :
        result = []
        z = None
        if len(matrix1) != len(matrix2) :
            raise ValueError("Matrices must be the same size")
        for i in range(len(matrix1)) :
            if len(matrix1[i]) != len(matrix2[i]) :
                raise ValueError("Matrices must be the same size")
        else :
            for i in range(len(matrix1)) :
                z = []
                for j in range(len(matrix1)) :
                    z.append(matrix1[i][j] + matrix2[i][j])
                result.append(z)
        return result

obj = Vectors()
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
vector3 = [4, -5]
x = 9
print(obj.addition(vector1, vector2))
print(obj.scalar_multiplication(vector1, vector2))
print(obj.multiplication(vector1, x))
print(obj.multiplication(vector2, x))
print(obj.length(vector1))
print(obj.length(vector2))
print(obj.rube(vector3))

matrix1 = [
    [1, 2, 3],
    [3, 4, 6],
    [3, 1, 9]
]
matrix2 = [
    [1, 2, 3],
    [3, 4, 6],
    [3, 1, 9]
] 

obj1 = Matrices()
print(obj1.addition(matrix1, matrix2))
