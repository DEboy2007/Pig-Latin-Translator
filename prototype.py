pyg = 'ay'

original = input('Enter a phrase or word:')
str_list = original.split(" ")

final = ""

try:
    for original in str_list:
        word = original.lower()
        first = word[0]
        new_word = word+first+pyg
        new_word = new_word[1:len(new_word)]
        final += str(new_word)
        final += " "
except:
    print("Woah. That didn't work. Maybe check if you entered an invalid or empty string!")


print(final)