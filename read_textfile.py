"""This module returns the contents of any unicode text file. """

from collections import Counter
__author__ = "5792397: James Brückheimer, 6769154: Mascha Magin"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mascha.magin@gmail.com"


class Reader:
    def __init__(self, textfile):
        self.textfile = textfile

    def read_textfile(self, textfile):
        """this function will return the text of a text file
        encoded in unicode. To import the file,
        the function takes its name as required argument
        when called. """
        try:
            text = open(textfile, "r", encoding = "utf-8").read()
        except:
            try:
                text = open(textfile, "r", encoding = "utf-16").read()
            except:
                text = open(textfile, "r", encoding = "utf-32").read()

        return text


class Text:
    def __init__(self, some_string):
        self.some_string = some_string

    def number_of_characters(self, some_string):
        return len(some_string) - some_string.count("\n")

    def number_of_words(self, some_string):
        """This function takes a string as argument and returns
        the number of the contained words, as it splits up the string
         into words after every blank space of the string.
         it then stores every word as one element in a list
         and returns the total of elements. """
        return len(some_string.split()) - some_string.count("–")

    def number_of_letters(self, some_string):
        return len(some_string) - some_string.count(" ") - some_string.count("\n")

    def count_of_characters(self, some_string):
        text = some_string.replace("\n", "")
        return Counter(text)

    def count_of_words(self, some_string):
       text = some_string.replace("\n", " ")
       text = text.replace("–", " ")
       text = text.replace(".", " ")
       text = text.replace("!", " ")
       text = text.replace(",", " ")
       text = text.split(" ")
       while "" in text:
           text.remove("")

       return Counter(text)

    def medium_length_of_words(self, some_string):
        text = some_string.replace("\n", " ")
        text = text.replace("–", " ")
        text = text.replace(".", " ")
        text = text.replace("!", " ")
        text = text.replace(",", " ")
        text = text.split(" ")
        while "" in text:
            text.remove("")
        for elem in text:
            a = (sum(len(elem)))
        return a / len(text)







output = Reader("Morgen_Kinder.txt")
text = str(output.read_textfile("Morgen_Kinder.txt"))
string = Text(str(output.read_textfile("Morgen_Kinder.txt")))

print("Number of characters in text file: ", string.number_of_characters(text), "\n"
      "Number of words in text file: ", string.number_of_words(text), "\n"
      "Number of letters in text file: ", string.number_of_letters(text), "\n"
      "Count of characters in text file: ", string.count_of_characters(text), "\n"
      "Count of words in text file: ", string.count_of_words(text), "\n"
      "Medium length of words: ", string.medium_length_of_words(text))
