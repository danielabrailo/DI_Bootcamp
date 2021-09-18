import anagram_checker

flag = True
while flag:
    menu = input('Write a word to find its anagrams, or press X to exit:\n')
    menu = menu.strip()  # Removing whitespace on both ends
    if menu.lower() == 'x':  # If user wants to exit the program
        flag = False
    elif len(menu.split()) > 1:  # If user inputs more than 1 word
        print('Only one word is accepted')
        continue
    elif not menu.isalpha():  # If user inputs something other than alphabetic word
        print('Only alphabet letters are accepted!')
        continue
    else:  # Correct input
        anagram_function = anagram_checker.AnagramChecker()
        if not anagram_function.is_valid_word(menu):
            print('This is not a valid word')
            continue
        else:
            anagrams_list = anagram_function.get_anagrams(menu)
            print(
                f'Your word is {menu} \nThis is a valid English word\nAnagrams for your word: {" ".join(anagrams_list)}')
