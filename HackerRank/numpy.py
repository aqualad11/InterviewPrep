import numpy 

# Arrays. A NumPy array is a grid of values. They are similar to lists, except that every element 
# of an array must be the same type.

a = numpy.array([1,2,3,4,5])
b = numpy.array([1,2,3,4,5], float)


# shape. The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
# using shape to get array dimensions
1D_array = numpy.array([1,2,3,4,5])
print(1D_array.shape) # (5,0) -> 5 rows and 0 columns

2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(2D_array.shape) # (3,2) -> 3 rows and 2 columns


# using shape to change array dimensions
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
'''
[[1 2]
[3 4]
[5 6]]
'''

# reshape 
# The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
arr = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(arr,(3,2)))

#Output
'''
[[1 2]
[3 4]
[5 6]]
'''

# transpose. Flip matrix on it's diagonal
2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
arr = numpy.transpose(2D_array)
print(arr)

# Flatten. flattens array to one dimension
arr = 2D_array
print(arr.flatten())


# Concatenate
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
# [1 2 3 4 5 6 7 8 9]

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
#[[1 2 3 0 0 0]
# [0 0 0 7 8 9]]  


# zeros. initializes numpy.array with zeros
print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

# ones. initializes numpy.array with zeros
print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]  