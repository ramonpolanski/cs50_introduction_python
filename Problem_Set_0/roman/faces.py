# defining main function as an input prompt and calling the convert function setting the input as the argument

def main():
    sentence = str(input("Enter a sentence including emoticons: "))
    convert(sentence)

# defining the convert function with the text argument and using the replace method to replace the emoticon with the emoji

def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

# calling the main function

main()