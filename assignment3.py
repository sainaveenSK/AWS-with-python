str1 = "i want"
str2 = "to live"
concatenated_string = str1 + " " + str2
print("Concatenated string:", concatenated_string)


name = "Nico Robin"
age = 18
format_string = "Name: %s, Age: %d" % (name, age)
print("Formatted string:", format_string)


from string import Template
template = Template("Name: $name, Age: $age")
format_string = template.substitute(name=name, age=age)
print("Formatted string:", format_string)


format_string = "Name: {}, Age: {}".format(name, age)
print("Formatted string:", format_string)


result_add = 98 + 89
print("Addition result:", result_add)


result_sub = 96 - 23
print("Subtraction result:", result_sub)

result_exp = 2 ** 5
print("Exponentiation result:", result_exp)


result_mod = 78 % 2
print("Modulus result:", result_mod)


h = 100
h -= 5
print("After subtraction assignment:",h)


r = 6
r *= 4
print("After multiplication assignment:",r)


w = 40
w /= 10
print("After division assignment:",w)

