def Punctuation(wd):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in wd.lower():
        if x in punctuations:
            wd = wd.replace(x,"")
    print(wd)

wd = input("Enter Word: ")
Punctuation(wd)