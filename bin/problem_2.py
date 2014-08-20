import proj_eul.math_functions.fibo

fib = proj_eul.math_functions.fibo.fib_list

n = int(raw_input("Please enter the integer parameter: "))
# n = 50

li = fib(n)

x = 0
for i in li[2::3]:
        x += i

print x
