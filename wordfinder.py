"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        wordfile = open(path)
        self.words = self.parse(wordfile)
        print(f"{len(self.words)} words read")
    def parse(self, wordfile):
        return [w.strip() for w in wordfile]
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, wordfile):
        return [w.strip() for w in wordfile if w.strip() and not w.startswith("#")]
