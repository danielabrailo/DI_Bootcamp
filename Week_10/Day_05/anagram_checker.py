class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt') as f:
            self.text_file = f.read().split()

    # def is_valid_word(self, word):

    def get_anagrams(self, word):
        anagrams_list = []
        for item in self.text_file:
            if self.is_anagram(item, word):
                anagrams_list.append(item.lower())
        return anagrams_list

    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) == len(word2) and word2 != word1:
            word1 = sorted(word1)
            word2 = sorted(word2)
            if word1 == word2:
                return True
            else:
                return False


# test = AnagramChecker()
# print(test.get_anagrams('meat'))
