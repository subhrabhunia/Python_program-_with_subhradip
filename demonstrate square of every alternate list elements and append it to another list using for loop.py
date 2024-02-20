original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alternate_squares = []

for i in range(len(original_list)):
    if i % 2 == 1:  
        alternate_squares.append(original_list[i] ** 2)

print("Square of every alternate list elements:", alternate_squares)
