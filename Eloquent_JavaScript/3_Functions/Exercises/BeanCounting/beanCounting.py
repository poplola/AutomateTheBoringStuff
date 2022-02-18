from gettext import find
from itertools import count


def countBs(string, chr):

    return string.count(chr)


text = "I like Blue sky and Beach the Best!"
chrB = 'B'
char = 't'

print(f"The string {text} has {countBs(text, chrB)} '{chrB}'s")
print(f"The string {text} has {countBs(text, char)} '{char}'s")