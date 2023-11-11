import phantom_tollbooth
#This import allows the text from the other program phantom_tollbooth.py to be used in this one



def main():
    #this statement calls the import and the variable is assigned the entire string of the phantom_tollbooth
    original = phantom_tollbooth.get_text()

    #these statements remove spaces and symbols that appear in the original string
    #and these commands require a new string to be made each time
    first_text_change = original.strip()
    second_text_change = first_text_change.translate({ord(","): None})
    third_text_change = second_text_change.translate({ord("-"): None})
    fourth_text_change = third_text_change.translate({ord(";"): None})
    fifth_text_change = fourth_text_change.translate({ord("."): None})
    sixth_text_change = fifth_text_change.translate({ord('"'): None})
    seventh_text_change = sixth_text_change.translate({ord("?"): None})
    final_text_change = seventh_text_change.replace("\n", "")

    #these satements make every letter in the string become lowercase and converts the string into a list
    lowercase_book =final_text_change.lower()
    list_of_words = lowercase_book.split(" ")

    #this commented out code below is how I originally planned to remove the articles, conjunctions and pronouns
    #but I eventually realized it would be more efficient to make a list of the words that need to be removed
    #and make a looping statement to remove those words instead of doing it manually
    #while("the" in my_list):
    #    my_list.remove("the")
    
    #this list contains all the words that need to be removed to output the correct top 50 most used words
    removal_list =['the',"and","to","a","of","he","you","in",'"',"as","it","his","for","was",
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
    
    #these statements remove all the words that are in the removal_list from the list containing 
    #all the words in the story, and places the perserved words into a new list
    final_list = [] 
    for i in list_of_words: 
        if i in removal_list:
            continue
        else:
            final_list.append(i)
    
    #this statement organizes the list so that all the words are in alphabetical order
    final_list.sort()

    #these statements place the words and the number of times they occur into a dictionary
    dict_of_words = {}
    for word in final_list[0:]:
        if word in dict_of_words:
            dict_of_words[word] = dict_of_words[word] + 1
        else:
            dict_of_words[word] = 1 

    print()
    print('The 50 most used words and how many times they are used in this story are: ' )

    #this statement makes the final_list contain only the most used words 
    final_list = sorted(dict_of_words, key=dict_of_words.get, reverse=True)[:50]
    
    #these statements output the most used words and the number of times they occurs in the story
    for z in final_list:
        print(z,':', dict_of_words[z],)
  
    #End of Program

if __name__ == '__main__':
    main()