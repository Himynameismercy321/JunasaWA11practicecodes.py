while True:
    word = input("Enter a word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True
            break

    if found:
        print("character found")
    else:
        print("character not found")

    again = input("Try again/ (Y/N): ")
    if again.upper() != "Y":
        break