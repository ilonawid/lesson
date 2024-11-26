import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as name:
                result = name.read().lower()  # Перевод в нижний регистр
                result.translate(str.maketrans('', '', string.punctuation))  # Удаление пунктуации
                words = result.split()  # Разбивка на элементы списка
                all_words[file_name] = words
            return all_words

    def find(self, word):
        my_dict = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                my_dict[file_name] = 1 + words.index(word.lower())
        return my_dict

    def count(self, word):
        my_dict = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            number = words.count(word.lower())
            if number < 0:
                pass
            else:
                my_dict[file_name] = number
        return my_dict


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
