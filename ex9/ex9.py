


def norma(text):                                # Funk with one Argument

    #print(text.upper())                        # Not the same like one down
    #print(text)                                # Not the same like one up

    if text.upper() == text:                    # If the UPP.Argument is == normal 
        if text[-1] == ".":                     # If last character[-1] is "."
            text = text[:-1]                    # Then jest delete it[:-1]                   
        print(text.capitalize() + "!")          # And print things Capital and put "!"       
    else:                                   
        print(text.capitalize())            

norma("CAPS LOCK DAY IS OVER.")                 # Call the funk
norma("today is not caps lock day.")
norma("let us stay calm, no need to panic.")


