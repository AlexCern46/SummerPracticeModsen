def narcissistic(value):
    value_str = str(value)
    value_len = len(value_str)

    total = 0
    for digit in value_str:
        total += int(digit) ** value_len

    if total == value:
        return True
    return False


print(narcissistic(153))
print(narcissistic(1652))
print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
