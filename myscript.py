import numpy as np

def function(matrix1,matrix2):
    try:
        return matrix1 * matrix2
    except ValueError:
        print("matrices are not aligned")
        return None

my_matrix =np.identity(4)
second_matrix=np.random.random(size=(4,4))
print(function(my_matrix,second_matrix))
