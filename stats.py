import re
from collections import Counter

def compute_stats(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    char_count = len(text)
    reading_time = round(word_count / 200) # This is in minutes assuming an average reading speed of 200 wpm

    common_words = Counter(w.lower() for w in words).most_common(5)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "char_count": char_count,
        "reading_time": reading_time,
        "common_words": common_words
    }
