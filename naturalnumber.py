def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)  # Recursive call

print(sum_n(5))  
