squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}



celsius_temps = {'New York': 20, 'Los Angeles': 25, 'Chicago': 10}
fahrenheit_temps = {city: (temp * 9/5) + 32 for city, temp in celsius_temps.items()}
print(fahrenheit_temps)  # Output: {'New York': 68.0, 'Los Angeles': 77.0, 'Chicago': 50.0}
'''
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "orange": "orange"
}
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}.")

'''


original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}


multiplication_table = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}
print(multiplication_table)
'''{
    1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
    3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
    4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
    5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
}
'''