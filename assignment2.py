string = "dragon ball is the godfather of the anime"
capitalize_function = string.capitalize()
upper_function = string.upper()
lower_function = string.lower()
print("Capitalize function:", capitalize_function)
print("Replicated .upper() function:", upper_function)
print("Replicated .lower() function:", lower_function)


old_sequence = [525,647,291,850,926,10,60,75,6,8]
new_sequence = [num for num in old_sequence if num % 2 != 0]
print("Odd sequence:", new_sequence)


fruits = {'carrot': 65, 'mango': 90, 'pineapple': 45, 'tomato': 80, 'apple': 60, 'jackfruit': 100}
fruits_more_than_20 = {key: value for key, value in fruits.items() if value > 20}
print("Fruits with values more than 20:", fruits_more_than_20)

