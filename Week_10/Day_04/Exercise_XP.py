# Exercise 1
import json, random

words = []


def get_words_from_file():
    with open('sowpods.txt', 'r') as f:
        for line in f.readlines():
            words.append(line)


def get_random_sentence(length: int):
    sentence = ''.join([random.choice(words) for i in range(length)])
    print(sentence.lower())


def main():
    print('This program will create a random sentence')
    length = int(input('How long do you want the sentence to be? Must be 2~20\n'))
    if 1 < length < 21:
        get_words_from_file()
        get_random_sentence(length)
    else:
        print('Incorrect number!')


main()
