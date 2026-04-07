import re
import random

def rm_special(data):
    data = re.sub(r'https?://\S+|www\.\S+', '', data)
    data = re.sub(r'<.*?>', '', data)
    data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    return data

def clean(data):
    data = data.lower()
    data = rm_special(data)
    data = re.sub(r'\s+', ' ', data).strip()
    return data

def del_rand(words, p=0.2):
    if len(words) <= 1: return words
    
    new_words = [word for word in words if random.uniform(0, 1) > p]
    
    if len(new_words) == 0:
        return [random.choice(words)]
    return new_words

def swap_rand(words, n=1):
    new_words = words.copy()
    for _ in range(n):
        idx1, idx2 = random.sample(range(len(new_words)), 2)
        new_words[idx1], new_words[idx2] = new_words[idx2], new_words[idx1]
    return new_words

def shuf_rand(words):
    new_words = words.copy()
    random.shuffle(new_words)
    return new_words

def aug(text):
    words = text.split()
    choice = random.choice(['delete', 'swap', 'shuf'])
    
    if choice == 'delete':
        augmented = del_rand(words, p=0.15)
    elif choice == 'swap':
        augmented = swap_rand(words, n=2)
    else:
        augmented = shuf_rand(words, n=2)
    return " ".join(augmented)