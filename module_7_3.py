import re
class WordsFinder:
    def __init__(self,*files):
        self.file_names = list(files)
    def get_all_words(self) -> dict:
        self.all_words = dict()
        for file in self.file_names:
            with open(file, encoding="utf-8") as read_file:
                words_file = []
                r= read_file.read().split("\n")
                for words in r:
                    words = words.lower()
                    words = re.sub(pattern='[,.=!?;": - ]', repl=" ", string=words)
                    words = re.split(string=words, pattern=" ")
                    for word in words:
                        if word != "" and word != " ":
                            words_file.append(word)
                self.all_words[file] = words_file
        return self.all_words
    def find(self,word:str) -> dict:
        result = dict()
        word = word.lower()
        for names , all_word in self.all_words.items():
            num_word = 0
            for word_file in all_word:
                num_word += 1
                if word == word_file:
                    result[names] = num_word
                    break
        return result
    def count(self,word:str) -> dict:
        word = word.lower()
        result = dict()
        for names, all_word in self.all_words.items():
            quantity = 0
            for words  in all_word:
                if words == word:
                    quantity += 1
            if quantity > 0:
                result[names] = quantity
        return result

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
    #________
    print()
    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    print(finder1.get_all_words())
    print(finder1.find('Child'))
    print(finder1.count('Child'))
    #_____________
    print()
    finder3 = WordsFinder('Rudyard Kipling - If.txt', )
    print(finder3.get_all_words())
    print(finder3.find('if'))
    print(finder3.count('if'))
    #_____________
    print()
    finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder4.get_all_words())
    print(finder4.find('captain'))
    print(finder4.count('captain'))


