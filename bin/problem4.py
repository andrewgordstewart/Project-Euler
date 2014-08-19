from project_euler.string_tools.palindrome import is_palindrome

pal = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(str(i*j)) and i*j > pal:
            pal = i*j


print pal
