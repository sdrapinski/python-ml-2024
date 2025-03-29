#type conversion

print(type(str(5)))
#escape sequence
weather= 'it\'s kinda sunny \n new line'
#print(weather)

name ="john"
surname="dohn"
# print(f"Hi {name} {surname}")

#string indexing
indexing = "0123456789"

print(indexing[::-1]) #reverse
#lists

array = [0,1,2,3,4,5,6,7]
print(array[0::2])

arr_copy = array[:]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])

print(len(matrix))

matrix.append([1,2,3])
print(matrix)

matrix.insert(3,100)
print(matrix)

matrix.pop()

print(matrix)
matrix.remove(100)

letters = ['a','b','c']
print(letters.index('a'))

print('c' in letters)
print(letters.count('a'))
letters.extend(['d','c','e'])
print(letters)
letters.sort()
print(letters)
print(letters[::-1])
print(list(range(0,100)))

dictionary = {
    'a':1,
    'b':2
}

print(dictionary['a'])