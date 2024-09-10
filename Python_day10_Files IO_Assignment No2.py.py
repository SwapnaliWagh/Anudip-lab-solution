#2.Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words():
    #Open the file "ABC.txt" in read mode
    file = open("ABC.txt", "r")
    
    #Initialize a variable to keep track of the word count
    word_count = 0
    
    #Loop through each line in the file
    for line in file:
        #Split the line into words using space as a delimiter
        words = line.split()
        
        #Add the number of words in this line to the total word count
        word_count += len(words)
    
    #Close the file after reading
    file.close()
    
    #Print the total number of words found in the file
    print(f"Total number of words in the file: {word_count}")

#Call the function to count and display the total number of words in "ABC.txt"
count_words()

"""ANS=>>

       Total number of words in the file: 3"""
       