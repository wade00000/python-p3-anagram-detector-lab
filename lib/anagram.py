# your code goes here!
class Anagram():
    def __init__(self,word):
        self.word = word.lower()

    def match(self,word_list):
        sorted_word = sorted(self.word)
        matches = []

        for term in word_list:
            if term.lower() != self.word and sorted(term) == sorted_word:
                matches.append(term)

        return matches
    
beast = Anagram("beast")
print(beast.match(["abets","baste","betas","beast","beats"]))

        
        