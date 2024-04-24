# Matrix
# Solution: understanding the problem, creating shallow copy so 
# each copy has a unique id

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
matrix[2][0] = "O"
print(matrix) # [

#['X', '-', '-'], 
#['X', '-', '-'], 
#['X', '-', '-']
#]

print(id(matrix[0][0]))
print(id(matrix[1][0]))
print(id(matrix[2][0]))