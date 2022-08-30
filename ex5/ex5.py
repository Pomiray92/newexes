


def inator(name):
    woc = ("a", "e", "i", "o", "u")
    if name.endswith(woc):
        print("inatorInator" + "('" + name + "')", " ->", name + "inator", len(name))
    else:
        print("inatorInator" + "('" + name + "')", " ->", name + "-inator")

name = input("Enter a name: ")

inator(name)