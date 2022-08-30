
def sirch(text_to_search_in, find_this_word):                   # The func has two Arguments
    if find_this_word in text_to_search_in:                     # If first Arg in second Arg
        place = text_to_search_in.find(find_this_word)          # To finding the place of second Argument
        print(f"I am found {find_this_word} at {place} !")      # Printing
    else:
        print(f"I can't find {find_this_word} :(")    



sirch("I am finding Nemo !", "Nemo")                            # Call the func
sirch("Nemo is me", "Nemo")
sirch("hallo ich bin Peer", "Peer")
sirch("Das ist nicht Nemo", "Nemo")
 