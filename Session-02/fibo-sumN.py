def fibo_sum(n):
    x = 0
    y = 1
    fibo_list = [x, y]
    for i in range (0, n - 1):
        fn = x + y
        fibo_list.append(fn)
        x = y
        y = fn
    return fibo_list

print('The sum of the first 5 Fibonacci series is:', sum(fibo_sum(5)))
print('The sum of the first 10 Fibonacci series is:', sum(fibo_sum(10)))