even_numbers = list(range(2,21,2))
print (even_numbers)
squares = []
for value in (range(1,21)):
    square = value ** 2
    squares.append(square)
print (squares)
cubes = [value ** 3 for value in range(1,21)]
print (cubes)

