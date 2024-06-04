def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    else:
        for i in range(3, n):
            signature.append(sum(signature[-3:]))
        return signature


print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 1))
print(tribonacci([0, 0, 0], 0))
