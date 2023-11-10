import phantom_tollbooth
from collections import Counter


book = phantom_tollbooth.get_text()

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

book1 = book.translate({ord(","): None})
book2 = book1.translate({ord("-"): None})
book3 = book2.translate({ord(";"): None})
book4 = book3.translate({ord("."): None})
book5 = book4.translate({ord('"'): None})
book6 = book5.translate({ord("?"): None})

my_list = Counter(book6.lower().split())

for word in set(remove_list):
    del my_list[word]

most_occur = my_list.most_common(50) 
print()
print('The 50 most used words and how many times they are used in this story are: ')
print() 
print(*most_occur, sep='\n')