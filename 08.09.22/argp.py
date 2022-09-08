# import argparse

# def sey_hello(args):                                    # Funk mit der "Parser(args)" argument
#     if args.name:                                       # Gucken ob die argumente eingegeben worden
#         print(f"Hallo {args.name}!")                    # Wen dann argument(name) vergeben ist, ausgabe wird gemachr!
        
#     else:
#         print("Hallo unbekanter Freund! ")              # Wenn nichts eingegeben würde!

def main():                                             # Hauptfunktion
    parser = argparse.ArgumentParser()                  # Zugreifen auf das Argparse Modul, und rufe die Argument Parser
    parser.add_argument("--name")                       # var(parser) braucht Argument. in diesem fall (add_argument) und in klammer die (name)
    
    args = parser.parse_args()                          # Var(args) ist ein leere container um gefundene Argumente zu speichern.
    print(args)                                         # ZU Checken ob das funktioniert!
    #sey_hello(args)
    
    
if __name__ == "__main__":                              # mein funk wird immer dan aufgerufen wenn diese programm diereckt gestartet wird
    main()