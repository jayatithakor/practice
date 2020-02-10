import numpy as np
import pandas as pd
def function(matrix1,matrix2):
    try:
        return matrix1 * matrix2
    except ValueError:
        print("matrices are not aligned")
        return None


print(function(my_matrix,second_matrix))
my_matrix =np.identity(5)
second_matrix=np.random.random(size=(4,4))
print(my_matrix*second_matrix)

