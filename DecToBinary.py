def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    return ''.join(binary[::-1])


num = 10
print(f"The binary representation of {num} is: {decimal_to_binary(num)}")
