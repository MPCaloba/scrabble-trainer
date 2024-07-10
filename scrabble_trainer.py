import random

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

def find_replacement(original_word, word_list):
    candidates = [candidate for candidate in word_list if len(candidate) == len(original_word) and candidate[0] == original_word[0]]
    return random.choice(candidates) if candidates else original_word

def replace_words(sentence, word_list):
    sentence_words = sentence.split()
    replaced_words = [find_replacement(word, word_list) for word in sentence_words]
    return ' '.join(replaced_words)

if __name__ == "__main__":
    words = load_word_list('words_alpha.txt')
    sentence = input("Enter a sentence: ")
    new_sentence = replace_words(sentence, words)
    print(new_sentence)
