str1 = "I want"
str2 = "to live"
concatenate_string = str1 + " " + str2
print("Concatenated string:", concatenate_string)


name = "gray fullbuster"
age = 30
format_string = "Name: %s, Age: %d" % (name, age)
print("Formatted string (using % operator):", format_string)



format_string = "Name: {}, Age: {}".format(name, age)
print("Formatted string (using format() method):", format_string)
format_string = f"Name: {name}, Age: {age}"
print("Formatted string (using f-strings):", format_string)
from string import Template
template = Template("Name: $name, Age: $age")
format_string = template.substitute(name=name, age=age)
print("Formatted string (using template strings):", format_string)



result_add = 2 + 8
print("Addition result:", result_add)
result_sub = 79 - 9
print("Subtraction result:", result_sub)
result_mul = 4 * 67
print("Multiplication result:", result_mul)
result_div = 888 / 2
print("Division result:", result_div)
result_exp = 4 ** 6
print("Exponentiation result:", result_exp)
result_mod = 16 % 4
print("Modulus result:", result_mod)
k = 50
k-= 5  
print("After subtraction assignment:",k)
c = 8
c *= 1  
print("After multiplication assignment:",c)
m = 444
m/= 4  
print("After division assignment:",m)
