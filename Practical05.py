import math
import string
import sys

def read_file(filename):
    """
    Read the contents of a file and return the text.
    """
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data
    except IOError:
        print("Error opening or reading input file:", filename)
        sys.exit()

def get_words_from_line_list(text):
    """
    Split the text lines into words and return a list of words.
    """
    translation_table = str.maketrans(string.punctuation + string.ascii_uppercase, " " * len(string.punctuation) + string.ascii_lowercase)
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list

def count_frequency(word_list):
    """
    Count the frequency of each word and return a dictionary mapping words to their frequency.
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] += 1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_file(filename):
    """
    Calculate word frequencies for a file and return a dictionary mapping words to their frequency.
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    
    print("File", filename, ":")
    print(len(line_list), "lines,")
    print(len(word_list), "words,")
    print(len(freq_mapping), "distinct words")
    
    return freq_mapping

def dot_product(D1, D2):
    """
    Calculate the dot product of two dictionaries.
    """
    return sum(D1.get(key, 0) * D2.get(key, 0) for key in D1)

def vector_angle(D1, D2):
    """
    Calculate the angle in radians between two document vectors.
    """
    numerator = dot_product(D1, D2)
    denominator = math.sqrt(dot_product(D1, D1) * dot_product(D2, D2))
    return math.acos(numerator / denominator)

def document_similarity(filename_1, filename_2):
    """
    Calculate and print the similarity between two documents.
    """
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    print("The distance between the documents is: %0.6f (radians)" % distance)

# Driver code
document_similarity('GFG.txt', 'file.txt')
