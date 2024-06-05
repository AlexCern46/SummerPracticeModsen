def pig_it(text):
    text = text.split()

    for i in range(len(text)):
        if text[i].isalpha():
            text[i] = text[i][1:] + text[i][0] + 'ay'

    return ' '.join(text)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
