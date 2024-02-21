def cow_bull(slayer,dragon):
    cow = sum(s == g for s, g in zip(slayer,dragon))
    bull = sum(g in slayer for g in dragon) - cow
    return cow, bull
slayer = "helicopter"
dragon= "halo"
print(cow_bull(slayer,dragon))

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))
print(is_palindrome("hello"))

def fibonacci(n):
    fibo = [0, 1]
    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[:n]
print(fibonacci(10))


def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    return list(range(start, stop, step))
print(my_range(5))
print(my_range(2, 8, 2))
