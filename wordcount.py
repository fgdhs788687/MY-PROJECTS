def word_count(sentences):
    words=sentences.split()
    return len(words)

#USED INPUT FUNCTION TO GET THE INPUT FROM THE USER.
user_input=input("Enter your Sentence: ")

#COUNT THE WORD USING THE FUNCTION.
count_word=word_count(user_input)

#PRINT FUNCTION IS USED TO DISPLAY THE OUTPUT OR RESULT.
print(f"The given sentence contains {count_word} words.")