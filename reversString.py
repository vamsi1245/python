def reverse_words(s):
    return ' '.join(s.split()[::-1])

text = "Hello World from Python"
reversed_text = reverse_words(text)
print(reversed_text)  