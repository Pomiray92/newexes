
def sirch(text_to_search_in, find_this_word): # The func has two 
    if find_this_word in text_to_search_in:
        place = text_to_search_in.find(find_this_word)
        print(f"I am found {find_this_word} at {place} !")
    else:
        print(f"I can't find {find_this_word} :(")    



sirch("I am finding Nemo !", "Nemo")
sirch("Nemo is me", "Nemo")
sirch("hallo ich bin Peer", "Peer")
sirch("Das ist nicht Nemo", "Nemo")
 