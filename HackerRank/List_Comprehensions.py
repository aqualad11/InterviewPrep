# Example: You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y)
# This is the code if we dont use list comprehensions in Python.
'''
x = int ( raw_input()) 
y = int ( raw_input()) 
n = int ( raw_input()) 
ar = [] 
p = 0 
for i in range ( x + 1 ): 
	for j in range( y + 1): 
		if i+j != n:
			ar.append([]) 
			ar[p] = [ i , j ] 
			p+=1 
print ar

# Code using list comprehensions:
x = int ( raw_input()) 
y = int ( raw_input()) 
n = int ( raw_input()) 
print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
'''

if __name__ =='__main__':
	name = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
	score = [37.21, 37.21, 37.2, 41, 39]

	students = {}
	for i in range(len(name)):
		temp = str(score[i])
		if(temp in students):
			students[str(score[i])].append(name[i])
		else:
			students[str(score[i])] = [name[i]]

	score.sort()
	names = students[str(score[1])]
	names.sort()
	print(names)