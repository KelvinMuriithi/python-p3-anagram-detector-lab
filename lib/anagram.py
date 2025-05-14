class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            if sorted(candidate) == sorted(self.word) and candidate.lower() != self.word.lower():
                matches.append(candidate)
        return matches

anagram = Anagram("listen")
anagram.match(['enlists', 'google', 'inlets', 'banana'])

        
