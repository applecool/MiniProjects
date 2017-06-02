import urllib.request

def read_text():
    quotes = open("/Users/ShellZero/MiniProjects/CurseChecker/movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_curse(contents)


def check_curse(text):
    print("Text before",text)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    out = connection.read()
    print(out)
    connection.close()
    if "true" in out:
        print("Curse word detected")
    elif "false" in out:
        print("No curse word found")
    else:
        print("Could not scan document properly")

read_text()

