import duden

def next_letter(s):
    return chr((ord(s.upper()) + j - 65) % 26 + 65)


def encrypt():
    text = input("text eingeben: ")
    global j
    j = int(input("bei wie viel? "))
    splitted = [a for a in text]
    i = 0

    for letter in splitted:
        if letter.isalpha():
            splitted[i] = next_letter(letter)
        else:
            splitted[i] = " "

        result = ''.join(splitted)
        i += 1
    print(result)


def decrypt():
    text = input("text eingeben: ")
    splitted = [a for a in text]
    n = 26
    while n > 0:
        global j
        i = 0
        j = 1
        for letter in splitted:
            if letter.isalpha():
                splitted[i] = next_letter(letter)
            else:
                splitted[i] = " "

            result = ''.join(splitted)
            i += 1
        j += 1
        n -= 1
        if duden.search(result.lower()):
            print(result.title() + " <===")
        else:
            print(result.title())


encrypt()
decrypt()
