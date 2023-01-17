"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    @classmethod
    def __repr__(self):
       return  
       """
       WordFinder
            input_file
            words = [words in input file]
            countq
       """
    # initialize file to open words.txt file
    def __init__(self, input_file_path="words.txt"):
        self.input_file = open(input_file_path, "r")
        self.words = [word for word in self.input_file]
        self.input_file.seek(0)
        self.input_file.close()
        self.count = 0

    def print_all_words(self):
        """
            loop through each word in words
                add 1 to count 
                print(word)
            print(f"{self.count} words read plus a random number{randint(0, self.count)})
        """
        for word in self.words:
            self.count = self.count + 1 
            print(word)
        print(f'{self.count} words read plus a random number {randint(0, self.count)}')
        self.reset_count()

    def reset_count(self):
        """
        reset's count to 0 
        """
        self.count = 0

    def random(self):
        """
        prints a random word based on length of read words, reset's count
        """
        print(self.words[randint(0, (len(self.words) - 1 ))])
        self.reset_count()

class SpecialWordFinder(WordFinder):
    def __init__(self):
        super().__init__("space_words.txt")

    def print_words(self):
        for word in self.words:
            if  word.strip() and word.startswith("#") != True:
                print(word)