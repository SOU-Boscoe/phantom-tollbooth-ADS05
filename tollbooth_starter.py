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
    while('the' in my_list):
        my_list.remove('the')
    while('and' in my_list):
        my_list.remove("and")
    while("to" in my_list):
        my_list.remove("to")
    while("a" in my_list):
        my_list.remove("a")
    while("of" in my_list):
        my_list.remove("of")
    while("he" in my_list):
        my_list.remove("he")
    while("you" in my_list):
        my_list.remove("you")
    while("in" in my_list):
        my_list.remove("in")
    while('"' in my_list):
        my_list.remove('"')
    while("as" in my_list):
        my_list.remove("as")
    while("it" in my_list):
        my_list.remove("it")
    while("his" in my_list):
        my_list.remove("his")
    while("for" in my_list):
        my_list.remove("for")
    while("was" in my_list):
        my_list.remove("was")
    while("that" in my_list):
        my_list.remove("that")
    while("i" in my_list):
        my_list.remove("i")
    while("all" in my_list):
        my_list.remove("all")
    while("said" in my_list):
        my_list.remove("said")
    while("with" in my_list):
        my_list.remove("with")
    while("they" in my_list):
        my_list.remove("they")
    while("at" in my_list):
        my_list.remove("at")
    while("one" in my_list):
        my_list.remove("one")
    while("but" in my_list):
        my_list.remove("but")
    while("be" in my_list):
        my_list.remove("be")
    while("on" in my_list):
        my_list.remove("on")
    while("is" in my_list):
        my_list.remove("is")
    while("had" in my_list):
        my_list.remove("had")
    while("from" in my_list):
        my_list.remove("from")
    while("have" in my_list):
        my_list.remove("have")
    while("very" in my_list):
        my_list.remove("very")
    while("what" in my_list):
        my_list.remove("what")
    while("them" in my_list):
        my_list.remove("them")
    while("were" in my_list):
        my_list.remove("were")
    while("there" in my_list):
        my_list.remove("there")
    while("up" in my_list):
        my_list.remove("up")
    while("so" in my_list):
        my_list.remove("so")
    while("then" in my_list):
        my_list.remove("then")
    while("not" in my_list):
        my_list.remove("not")
    while("see" in my_list):
        my_list.remove("see")
    while("can" in my_list):
        my_list.remove("can")
    while("just" in my_list):
        my_list.remove("just")
    while("do" in my_list):
        my_list.remove("do")
    while("are" in my_list):
        my_list.remove("are")
    while("if" in my_list):
        my_list.remove("if")
    while("now" in my_list):
        my_list.remove("now")
    while("we" in my_list):
        my_list.remove("we")
    while("an" in my_list):
        my_list.remove("an")
    while("no" in my_list):
        my_list.remove("no")
    while("who" in my_list):
        my_list.remove("who")
    while("time" in my_list):
        my_list.remove("time")
    while("which" in my_list):
        my_list.remove("which")
    while("this" in my_list):
        my_list.remove("this")
    while("again" in my_list):
        my_list.remove("again")
    while("more" in my_list):
        my_list.remove("more")
    while("or" in my_list):
        my_list.remove("or")
    while("it's" in my_list):
        my_list.remove("it's")
    while("here" in my_list):
        my_list.remove("here")
    while("when" in my_list):
        my_list.remove("when")
    while("how" in my_list):
        my_list.remove("how")
    while("i'm" in my_list):
        my_list.remove("i'm")
    while("my" in my_list):
        my_list.remove("my")
    while("much" in my_list):
        my_list.remove("much")
    while("way" in my_list):
        my_list.remove("way")
    while("down" in my_list):
        my_list.remove("down")
    while("like" in my_list):
        my_list.remove("like")
    while("don't" in my_list):
        my_list.remove("don't")
    while("me" in my_list):
        my_list.remove("me")
    while("by" in my_list):
        my_list.remove("by")
    while("never" in my_list):
        my_list.remove("never")
    while("could" in my_list):
        my_list.remove("could")
    while("into" in my_list):
        my_list.remove("into")
    while("back" in my_list):
        my_list.remove("back")
    while("your" in my_list):
        my_list.remove("your")
    while("little" in my_list):
        my_list.remove("little")
    while("long" in my_list):
        my_list.remove("long")
    while("out" in my_list):
        my_list.remove("out")
    while("him" in my_list):
        my_list.remove("him")
    while("well" in my_list):
        my_list.remove("well")
    while("been" in my_list):
        my_list.remove("been")
    while("why" in my_list):
        my_list.remove("why")
    while("that's" in my_list):
        my_list.remove("that's")
    while("where" in my_list):
        my_list.remove("where")
    while("would" in my_list):
        my_list.remove("would")
    while("only" in my_list):
        my_list.remove("only")
    while("she" in my_list):
        my_list.remove("she")
    while("know" in my_list):
        my_list.remove("know")
    while("off" in my_list):
        my_list.remove("off")
    while("their" in my_list):
        my_list.remove("their")
    while("other" in my_list):
        my_list.remove("other")
    while("too" in my_list):
        my_list.remove("too")
    while("each" in my_list):
        my_list.remove("each")
    while("right" in my_list):
        my_list.remove("right")
    while("about" in my_list):
        my_list.remove("about")
    while("even" in my_list):
        my_list.remove("even")
    while("good" in my_list):
        my_list.remove("good")
    while("must" in my_list):
        my_list.remove("must")
    while("than" in my_list):
        my_list.remove("than")
    while("many" in my_list):
        my_list.remove("many")
    while("after" in my_list):
        my_list.remove("after")
    while("get" in my_list):
        my_list.remove("get")
    while("once" in my_list):
        my_list.remove("once")
    while("make" in my_list):
        my_list.remove("make")
    while("over" in my_list):
        my_list.remove("over")
    while("three" in my_list):
        my_list.remove("three")
    while("day" in my_list):
        my_list.remove("day")
    while("look" in my_list):
        my_list.remove("look")
    while("through" in my_list):
        my_list.remove("through")
    while("any" in my_list):
        my_list.remove("any")
    while("before" in my_list):
        my_list.remove("before")
    while("great" in my_list):
        my_list.remove("great")
    while("most" in my_list):
        my_list.remove("most")
    while("always" in my_list):
        my_list.remove("always")
    while("take" in my_list):
        my_list.remove("take")
    while("another" in my_list):
        my_list.remove("another")
    while("himself" in my_list):
        my_list.remove("himself")
    while("same" in my_list):
        my_list.remove("same")
    while("some" in my_list):
        my_list.remove("some")
    while("two" in my_list):
        my_list.remove("two")
    while("did" in my_list):
        my_list.remove("did")
    while("come" in my_list):
        my_list.remove("come")
    while("didn't" in my_list):
        my_list.remove("didn't")
    while("ever" in my_list):
        my_list.remove("ever")
    while("go" in my_list):
        my_list.remove("go")
    while("place" in my_list):
        my_list.remove("place")
    while("thing" in my_list):
        my_list.remove("thing")
    while("until" in my_list):
        my_list.remove("until")
    while("will" in my_list):
        my_list.remove("will")
    while("say" in my_list):
        my_list.remove("say")
    while("made" in my_list):
        my_list.remove("made")
    while("went" in my_list):
        my_list.remove("went")
    while("use" in my_list):
        my_list.remove("use")
    while("can't" in my_list):
        my_list.remove("can't")
    while("old" in my_list):
        my_list.remove("old")
    while("first" in my_list):
        my_list.remove("first")
    while("last" in my_list):
        my_list.remove("last")
    while("since" in my_list):
        my_list.remove("since")
    while("" in my_list):
        my_list.remove("")
    while("you'll" in my_list):
        my_list.remove("you'll")
    while("oh" in my_list):
        my_list.remove("oh")
    while("still" in my_list):
        my_list.remove("still")

    my_list.sort()
    my_dict = {}
    

    for word in my_list[0:]:
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1 

    print()
    print('The 50 most used words and how many times they are used in this story are: ' )

    my_list = sorted(my_dict, key=my_dict.get, reverse=True)[:50]

    for x in my_list:
        print(x,':', my_dict[x],)
  
if __name__ == '__main__':
    main()