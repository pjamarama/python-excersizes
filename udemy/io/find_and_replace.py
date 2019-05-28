'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

# def  find_and_replace(file, find_word, replace_word):
#     fi = open (file, 'r+')
#     text = fi.read()
#     fi.seek(0)
#     fi.write(text.replace(find_word, replace_word))
#     fi.close()

def  find_and_replace(file, find_word, replace_word):
    with open(file, 'r+') as fi:
        text = fi.read()
        fi.seek(0)
        fi.write(text.replace(find_word, replace_word))


find_and_replace('short.txt', 'Alex', 'Mickleton')



'''
str.replace("is", "was")
file.write(str)
'''