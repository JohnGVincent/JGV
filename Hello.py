# Open the word file as RT
file = open("word_list.txt", "rt")
data = file.read()

#Seperate the file contents into individual elements
words = data.split()
#count the number of words in the list, 
#it allows me to change the number of words in the list later
word_list_length = len(words)

print('Number of words in text file :', len(words))
#Access the sys/random modules
import sys
import random

#produce an indexing random number between 0 and word_list_length-1
key_num = random.SystemRandom()
selection = random.randint(0,(word_list_length-1))
#If it all goes wrong! print (selection)

#Select a word based on the random selection
hang_word = (words[selection])
word_length = len(hang_word)
#If it all goes wrong! print (hang_word)
#print (word_length)

#Start to generate the unknown letters - there must be at least one letter in the string !
word_blanks = "*"
#While loop to generate the rest of the letters - concatenate the extra stars one at a time
loop_count = word_length
while (loop_count > 1):     
    loop_count = loop_count - 1
    word_blanks = word_blanks + "*"

#Start a loop of seven tries(wrong guesses) to loop until either..
#...all 7 tries are exhausted or the word is guessed correctly
try_count = 7
print (word_blanks)
while (try_count > 0) and (word_blanks!=hang_word):
    
    letter_choice = input ("Enter a letter :")
    #Strings are imutable so I'll have to regenerate the string from scratch, it looks backwards
    temp_word_blanks = word_blanks
    word_blanks = ""
    #Start another loop to test each letter in turn to see if it matches 
    loop_count=0
    while (loop_count < word_length):
        #first test if the character has already been correctly guessed, if so leave it so
        if temp_word_blanks[loop_count] != "*":
           word_blanks = word_blanks + temp_word_blanks[loop_count] 
        #otherwise test if the choice matches the current character
        else:
            if hang_word[loop_count] == letter_choice:
               word_blanks = word_blanks + letter_choice
            else: 
                word_blanks = word_blanks + "*"
                
        loop_count = loop_count + 1
    if word_blanks == temp_word_blanks:
        try_count = try_count -1    
    print (str(try_count), "tries left")
    print (word_blanks)

#While loop has been exited, so either the word has been correctly guessed or all tries exhausted    
else:
    if (word_blanks==hang_word) :
        print ("Well done you win !")
    else :
        print (" Out of tries")