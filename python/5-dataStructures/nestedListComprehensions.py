#transpose of a matrix


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print('original matrix :',matrix)



transpose=[[row[i] for row in matrix] for i in range(3)]
print('transposed matrix: ',transpose)

print('transposed again the matrix using built in zip function: ',list(zip(*matrix)))

