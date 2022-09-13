import argparse

def name_age_last(args):                                                                              # Funk mit der "Parser(args)" argument
    if args.first:                                                                      
        print(f"Hello {args.first} {args.last}! I see that you have had {args.age} birthdays.")
    elif args.first == (""):
        args.first = "Larry"
    if args.last:
        print(f"Hello {args.first} {args.last}! I see that you have had {args.age} birthdays.") 
    elif args.last== (""):
        args.last = "Henson"
    if args.age:
        print(f"Hallo {args.first}!I see that you have had {args.age} birthdays.")   
    elif args.age == (""):
        args.age = "100"
    else:                                                                                                    
        print("Hello Harry Henson! I see that you have had 100 birthdays.")
        
def main():                                                                                 # Hauptfunktion
    parser = argparse.ArgumentParser()                                                      # Zugreifen auf das Argparse Modul, und rufe die Argument Parser
    parser.add_argument("--first")                                                       # var(parser) braucht Argument. in diesem fall (add_argument) und in klammer die (name)
    parser.add_argument("--last")
    parser.add_argument("--age")
    
    args = parser.parse_args()                                                              # Var(args) ist ein leere container um gefundene Argumente zu speichern.
    #print(args)                                                                            # ZU Checken ob das funktioniert!
    name_age_last(args)
    
if __name__=='__main__':
    main()    

    
