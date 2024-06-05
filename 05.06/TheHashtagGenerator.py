def generate_hashtag(s):
    if len(s) == 0 or len(''.join(s.split())) > 139:
        return False
    else:
        return '#' + ''.join([word.capitalize() for word in s.split()])


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
