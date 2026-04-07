import re

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
