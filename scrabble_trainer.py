import random

def load_word_list(file_path):
    """
    Load words from a file and return them as a list.

    Args:
    file_path (str): The path to the file containing words.

    Returns:
    list: A list of words.
    """
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

def find_replacement(original_word, word_list):
    """
    Find a replacement word that starts with the same letter and is the same length as the given word.

    Args:
    original_word (str): The word to find a replacement for.
    word_list (list): The list of candidate words.

    Returns:
    str: A replacement word if found, otherwise the original word.
    """
    candidates = [candidate for candidate in word_list if len(candidate) == len(original_word) and candidate[0] == original_word[0]]
    return random.choice(candidates) if candidates else original_word

def replace_words(sentence, word_list):
    """
    Replace each word in the sentence with a randomly chosen word of the same length and starting letter.

    Args:
    sentence (str): The input sentence.
    word_list (list): The list of candidate words.

    Returns:
    str: The sentence with replaced words.
    """
    sentence_words = sentence.split()
    replaced_words = [find_replacement(word, word_list) for word in sentence_words]
    return ' '.join(replaced_words)

if __name__ == "__main__":
    """
    Main function that:
    1. Loads the words from the file
    2. Prompts the user to enter a sentence
    3. Replaces the words in the sentence
    4. Prints the new sentence
    """
    words = load_word_list('words_alpha.txt')
    sentence = input("Enter a sentence: ")
    new_sentence = replace_words(sentence, words)
    print(new_sentence)
