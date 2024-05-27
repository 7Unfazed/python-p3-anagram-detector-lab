# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if ''.join(sorted(anagram)) == self.sorted_word]


