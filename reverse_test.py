# x is a string representing a book of text. The pages are separatd by \b. The lines by \n. 

# Write a function that reverses the
# - order of pages \b
# - order of lines in each page \n
# - order of words in each line \s
# - don't reverse the characters in each word

# Sample string:
x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

def reverse_line(input):
    res = ""
    for word in input.split(" "):
        res = word + " " + res;
    return res

def reverse_page(input):
    res = ""
    for line in input.split("\n"):
        if not line: continue
        res = reverse_line(line) + "\n" + res
    return res

def reverse_book(input):
    res = ""
    for page in input.split("\b"):
        res = reverse_page(page) + "\b" + res
    return res


print(reverse_book(x))