from textblob import TextBlob
import pandas as pd
from collections import Counter
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def get_word_counts(lyrics, remove_stopwords=True):
    text = clean_text(' '.join(lyrics))
    words = text.split()
    if remove_stopwords:
        words = [w for w in words if w not in stop_words]
    return Counter(words)

def get_sentiments(df):
    sentiments = []
    for row in df.itertuples():
        blob = TextBlob(row.lyrics)
        sentiments.append(blob.sentiment.polarity)
    df['sentiment'] = sentiments
    return df
