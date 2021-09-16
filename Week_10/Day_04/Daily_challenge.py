# Text Analysis program
import string, re


class Text():
    def __init__(self, text: str):
        self.text = text

    def check_frequency(self, word: str):
        ocurrences = self.text.count(word)
        return ocurrences

    def most_common_word(self):
        frequency = 0
        for word in self.text:
            if self.check_frequency(word) > frequency:
                frequency = self.check_frequency(word)
                return word

    def unique_words(self):
        words_list = []
        for word in self.text:
            if self.check_frequency(word) == 1:
                words_list.append(word)
        print(words_list)


class TextModification(Text):
    def no_punctuation(self):
        new_text = re.sub(r'[^\w\s]', '', self.text)
        return new_text

    def no_stopwords(self):
        with open('stopwords') as file:
            stopwords_list = file.read().split()
            new_list = [i for i in self.text.split() if i not in stopwords_list]
            print(' '.join(new_list))


with open('the_stranger.txt') as f:
    file_text = f.read()

test = Text(file_text)
