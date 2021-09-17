import anagram_checker


flag = True
while flag:
    menu = input('Write a word to find its anagrams, or press X to exit:\n')
    if menu.lower() == 'x':
        flag = False
    else:
        anagram_function = anagram_checker.AnagramChecker()
        anagrams_list = anagram_function.get_anagrams(menu)
        print(f'Your word is {menu}')
        print(f'Anagrams for your word: {" ".join(anagrams_list)}')
