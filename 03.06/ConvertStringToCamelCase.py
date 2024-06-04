def to_camel_case(text):
    import re

    arr = re.split(r'[-_]', text)

    for i in range(1, len(arr)):
        arr[i] = arr[i].capitalize()

    return ''.join(arr)


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
