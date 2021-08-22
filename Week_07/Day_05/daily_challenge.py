words = input("Write a sequence of words separated by comas: ")
words_list = [word for word in words.split(",")]
words_list.sort()


print(f"The sorted order is: {words_list}")


