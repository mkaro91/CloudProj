import re
from collections import Counter

def generate_summary(text, num_sentences=3):

    if not text.strip():
        return ""
    
    # A set of common words that are not important for summarization and will be ignored when calculating sentence scores
    STOPWORDS = {
    "the", "is", "and", "of", "to", "a", "in", "that", "it", "on", "for", "as", "with", "was", "were"
}

    # Splits the text in the document up into an array of sentences (whenever a sentence ending punctuation appears)
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Strips whitespace from sentences and removes them if they are shorter than 20 characters as they won't have enough information to summarize
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    # If there are only a few useful then it will return all of the saved ones
    if len(sentences) <= num_sentences:
        return ' '.join(sentences)
    
    # Splits the sentences into individual words to determine word frequency if it's not in stopwords constant
    words = [w for w in re.findall(r'\b\w+\b', text.lower()) if w not in STOPWORDS]

    # Counts each individual word
    word_freq = Counter(words)

    # Initializing a variable that assigns a value to each sentence based on frequency of important word appearance
    sentences_scored = {}

    # Iterates through each sentence
    for i, sentence in enumerate(sentences):
        score = 0
        # Separates all the words in the sentence and returns an array containing the words in each sentence that are not in stopwords
        sentence_words = [w for w in re.findall(r'\b\w+\b', sentence.lower()) if w not in STOPWORDS]

        # Adds 
        for word in sentence_words:
            score += word_freq[word]
        if len(sentence_words) > 0:
            score = score / len(sentence_words)
        sentences_scored[i] = score

    top_sentences = sorted(sentences_scored, key=sentences_scored.get, reverse=True)[:num_sentences]
    top_sentences.sort()

    summary = ' '.join([sentences[i] for i in top_sentences])

    return summary