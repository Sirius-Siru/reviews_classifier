import re
from nltk import ngrams

def rm_special(data):
    data = re.sub(r'https?://\S+|www\.\S+', '', data)
    data = re.sub(r'<.*?>', '', data)
    data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    return data

def clean(data):
    data = data.str.lower()
    data = rm_special(data)
    data = re.sub(r'\s+', ' ', data).strip()
    return data

def tokenization(data):
    return data.split()

def to_bigrams(data):
    return list(ngrams(data, 2)) 