import phantom_tollbooth




def main():
    book3 = phantom_tollbooth.get_text()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    book2 = book3.strip()
    book1 = book2.translate({ord(","): None})
    book3 = book1.translate({ord("-"): None})
    book4 = book3.translate({ord(";"): None})
    book5 = book4.translate({ord("."): None})
    book6 = book5.translate({ord('"'): None})
    book7 = book6.translate({ord("?"): None})

    book = book7.replace("\n", "")
    for symbol in book:
        if symbol in punc:
            book.replace(symbol, "")
    final_book =book.lower()
    my_list = final_book.split(" ")
    
    for x in my_list:
        if x == int():
            my_list.remove(x)

    while("" in my_list):
        my_list.remove("")
    
    while('"' in my_list):
        my_list.remove('"')
    my_list.sort()
    my_dict = {}
    

    for word in my_list[0:]:
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1 
    
    my_list = sorted(my_dict, key=my_dict.get, reverse=True)[:50]
    for x in my_list:
        print(x,':', my_dict[x])
            

           




    
    

if __name__ == '__main__':
    main()