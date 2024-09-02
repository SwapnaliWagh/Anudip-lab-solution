#1. Write a Python program to count the occurrences of each word in a given sentence 
#string = “To change the overall look of your document. To change the look available in the gallery” 
# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Remove punctuation (if any) and convert the sentence to lowercase
sentence = sentence.replace('.', '').lower()

# Split the sentence into words
words = sentence.split()

# Create a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Print the occurrences of each word
for word, count in word_count.items():
    print(f"'{word}': {count}")


"""Ans=>
'to': 2
'change': 2
'the': 3
'overall': 1
'look': 2
'of': 1
'your': 1
'document': 1
'available': 1
'in': 1
'gallery': 1"""
