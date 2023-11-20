import string

def remove_stop_words(text):
    # Define a list of common English stop words
    stop_words = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
        "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
        "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
        "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
        "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
        "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
        "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn",
        "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"
    ])

    # Tokenize the text into words
    words = text.lower().split()

    # Remove punctuation
    words = [''.join(c for c in word if c not in string.punctuation) for word in words]

    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]

    # Join the filtered words back into a sentence
    preprocessed_text = ' '.join(filtered_words)

    return preprocessed_text

# Example usage
text_to_preprocess = "This is an example sentence for text preprocessing. It includes stop words, which we want to remove."

preprocessed_text = remove_stop_words(text_to_preprocess)

print("Original Text:")
print(text_to_preprocess)
print("\nPreprocessed Text:")
print(preprocessed_text)
