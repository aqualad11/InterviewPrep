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

# identity. The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
#[[ 1.  0.  0.]
# [ 0.  1.  0.]
# [ 0.  0.  1.]]

# eye. The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
#[[ 0.  1.  0.  0.  0.  0.  0.]
# [ 0.  0.  1.  0.  0.  0.  0.]
# [ 0.  0.  0.  1.  0.  0.  0.]
# [ 0.  0.  0.  0.  1.  0.  0.]
# [ 0.  0.  0.  0.  0.  1.  0.]
# [ 0.  0.  0.  0.  0.  0.  1.]
# [ 0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.  0.  0.]]


# mathematical functions
a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]


# floor. The tool floor returns the floor of the input element-wise
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

# ceil. The tool ceil returns the ceiling of the input element-wise.
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

# rint. The rint tool rounds to the nearest integer of input element-wise.
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]


# sum.The sum tool returns the sum of array elements over a given axis.
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

# prod. The prod tool returns the product of array elements over a given axis.

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24