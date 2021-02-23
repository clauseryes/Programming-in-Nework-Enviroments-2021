def fibon(n):
    x = 0
    y = 1
    fibo_list = [x, y]
    for i in range(0, n - 1):
        fn = x + y
        fibo_list.append(fn)
        x = y
        y = fn
    return fn

print('The 5th Fibonacci number is', fibon(5))
print('The 10th Fibonacci number is', fibon(10))
print('The 15th Fibonacci number is', fibon(15))