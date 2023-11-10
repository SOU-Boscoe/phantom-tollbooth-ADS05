import phantom_tollbooth
from collections import Counter

#this statement calls the import and the variable is assigned the entire string of the phantom_tollbooth
original_text = phantom_tollbooth.get_text()

#this list contains all the words that need to be removed to output the correct top 50 most used words
remove_list =['the',"and","to","a","of","he","you","in",'"',"as","it","his","for","was",
              "that","i","all","said","with","they","at","one","but","be","on","is","had",
              "from","have","very","what","them","were","there","up","so","then","not","see",
              "can","just","do","are","if","now","we","an","no","who","time","which","this",
              "again","more","or","it's","here","when","how","i'm","my","much","way","down",
              "like","don't","me","by","never","could","into","back","your","little","long",
              "out","him","well","been","why","that's","where","would","only","she","know",
              "off","their","other","too","each","right","about","even","good","must","than",
              "many","after","get","once","make","over","three","day","look","through","any",
              "before","great","most","always","take","another","himself","same","some","two",
              "did","come","didn't","ever","go","place","thing","until","will","say","made",
              "went","use","can't","old","first","last","since","","you'll","oh","still"]

#these statements remove spaces and symbols that appear in the original string
#and these commands require a new string to be made each time
text_change_1 = original_text.translate({ord(","): None})
text_change_2 = text_change_1.translate({ord("-"): None})
text_change_3 = text_change_2.translate({ord(";"): None})
text_change_4 = text_change_3.translate({ord("."): None})
text_change_5 = text_change_4.translate({ord('"'): None})
text_change_6 = text_change_5.translate({ord("?"): None})

#this statement makes all letters lowercase, converts the string into a list, and allows the list to be counted
list_of_words = Counter(text_change_6.lower().split())

#these statements remove all the words that are in the removal_list from the list containing 
#all the words in the story
for word in set(remove_list):
    del list_of_words[word]

#these statements calculate the 50 most common words and outputs them
most_occur = list_of_words.most_common(50) 
print()
print('The 50 most used words and how many times they are used in this story are: ')
print() 
print(*most_occur, sep='\n')

#End of Program