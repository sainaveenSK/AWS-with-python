name = "usopp"
upper_case = name.upper()
print("Upper case:", upper_case)
lower_case = name.lower()
print("Lower case:", lower_case)
capitalized = name.capitalize()
print("Capitalized:", capitalized)
replaced = name.replace('u', 'U')
print("Replaced:", replaced)



L = [9,5,2]
L.extend([7,4,3])
del L[4]
print("Extended list:", L)


d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}
out_of_stock = [key for key, value in d.items() if value == 0]
for fruit in out_of_stock:
    del d[fruit]
d['mango'] = 15
d['pineapple'] -= 5
print("Updated dictionary:", d)



a = [20, 40, 60, 80, 100]
a += [14, 16, 18, 12]
print(a)


a[:] = [-i for i in a][::-1] + [0]
print(a)


a[:] = [2, 3, 4, 5, 6, 7, 8, 9]
print(a)


a[3:3] = ['f', 'd', 'o']
print(a)



a = a
print(a)



a[0:0] = []
print(a[0:0])
print(a[::-1])
print(a[0:3])
print(a[2:])


a[1:4] = []
print(a)
print(a[1:4])


a[-1:] = a[1:] + [12, 14, 16, 18, 20]
print(a)
