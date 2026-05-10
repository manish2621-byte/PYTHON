# Write a Python program to demonstrate string slicing

text = "Python Programming"


print("Original String:", text)
print("First word:", text[0:6])

print("From index 7:", text[7:])


print("Last word:", text[-11:])


print("Skipping characters:", text[0:18:2])

print("Reversed string:", text[::-1])

# Write a Python program that manipulates and prints strings using various string methods.


text = "  python programming is fun  "

# Original string
print("Original String:", text)

# 1. Remove extra spaces
clean_text = text.strip()
print("After strip():", clean_text)

print("Uppercase:", clean_text.upper())

print("Lowercase:", clean_text.lower())

print("Capitalized:", clean_text.capitalize())

print("Title Case:", clean_text.title())

replaced_text = clean_text.replace("fun", "awesome")
print("After replace():", replaced_text)

print("Length:", len(clean_text))

print("Contains 'python':", "python" in clean_text)