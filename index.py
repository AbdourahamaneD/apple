def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation+="python"
        else:
            translation+=letter
    return translation
print(translate(input("entrer une phrase:")))