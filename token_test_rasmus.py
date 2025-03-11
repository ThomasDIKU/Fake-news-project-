import re
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Læs data
data = pd.read_csv("995,000_rows.csv", dtype =str, nrows=10000)
# Antal rækker, tilføj: ",nrows=10_000" til ovenstående linje)

# Kompiler regex
date_regex = re.compile(r"""
\b(
    (?:\d{1,2}[./-]\d{1,2}[./-]\d{2,4}) |
    (?:\d{4}[./-]\d{1,2}[./-]\d{1,2}) |
    (?:\b\d{1,2}(st|nd|rd|th)?\s+(of\s+)?[A-Za-z]+\s+\d{4}\b) |
    (?:\b[A-Za-z]+\s+\d{1,2}(st|nd|rd|th)?,?\s+\d{4}\b) |
    (?:\b[A-Za-z]+\s+\d{4}\b)
)\b
""", re.VERBOSE | re.IGNORECASE)
number_regex = re.compile(r'\d+')
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
url_regex = re.compile(r'\b(?:http[s]?://|www\.)[^\s<>"]+\b')
whitespace_regex = re.compile(r'\s+')

def clean_text(text):
    text = str(text).lower()
    text = re.sub(whitespace_regex, ' ', text)
    text = re.sub(date_regex, "<DATE>", text)
    text = re.sub(url_regex, "<URL>", text)
    text = re.sub(email_regex, "<EMAIL>", text)
    text = re.sub(number_regex, "<NUM>", text)
    return text

# Rens data
regex_clean_data = data['content'].astype(str).apply(clean_text)

# Tokenizér
tokens = word_tokenize(' '.join(regex_clean_data))

# Beregn ordforrådsstørrelse før stopord
vocab_before = len(set(tokens))

# Fjern stopord
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]

# Beregn ordforrådsstørrelse efter stopord
vocab_after_stop = len(set(filtered_tokens))

# Beregn reduktionsrate
stopword_reduction = ((vocab_before - vocab_after_stop) / vocab_before) * 100

print(f"Vocabulary before stopword removal: {vocab_before}")
print(f"Vocabulary after stopword removal: {vocab_after_stop}")
print(f"Reduction rate after stopword removal: {stopword_reduction:.2f}%")

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens if word.isalpha()]

# Beregn ordforrådsstørrelse efter stemming
vocab_after_stemming = len(set(stemmed_tokens))

# Beregn reduktionsrate efter stemming
stemming_reduction = ((vocab_before - vocab_after_stemming) / vocab_before) * 100

print(f"Vocabulary after stemming: {vocab_after_stemming}")
print(f"Reduction rate after stemming: {stemming_reduction:.2f}%")


# Calculate word frequency
def word_frequency(data):
    word_freq = {}
    for word in data:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Sort the vocabulary by frequency
def freq_sort(data):
    return dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

sorted_top_vocab = freq_sort(word_frequency(stemmed_tokens))

print(sorted_top_vocab) # Print the sorted vocabulary

def plot_top_words(data):
    # Get the 50 most common words
    top_50 = list(sorted_top_vocab.items())[:50]

    # Separate words and frequencies
    words, frequencies = zip(*top_50)

    # Plot the bar chart
    plt.figure(figsize=(14, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 50 Most Frequent Words')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_top_words(sorted_top_vocab)