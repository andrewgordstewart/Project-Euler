import project_euler.math_functions.fibo

fib = project_euler.math_functions.fibo.fib_list

li = fib(4000000)

x = 0
for i in li:
    if i % 2 == 0:
        x += i

print x
