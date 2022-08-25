

def fun1(name):
    woc = ("a", "e", "i", "o", "u")
    if name.endswith(woc):    
        result = name, "inator", str(len(name)), "000"
        print("inatorInator", "(", name + ")", " -> ", result)
    else:
        result = name,"-inator", str(len(name)), "000"
        print("inatorInator", "(", name, ")", " -> ", result)

def run(): 
    name = input(str("enter something: "))  
    fun1(name)    

run()