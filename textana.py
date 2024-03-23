#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())
    
    # Remove punctuation and stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    return words

def calculate_sentiment(text, positive_words, negative_words):
    cleaned_text = clean_text(text)
    
    # Calculate positive and negative scores
    positive_score = sum(1 for word in cleaned_text if word in positive_words)
    negative_score = sum(1 for word in cleaned_text if word in negative_words)
    
    # Calculate polarity score
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    
    # Calculate subjectivity score
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_text) + 0.000001)
    
    return positive_score, negative_score, polarity_score, subjectivity_score

def analyze_readability(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Calculate average sentence length
    avg_sentence_length = sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences)
    
    # Calculate percentage of complex words
    words = clean_text(text)
    complex_words = [word for word in words if len(word) > 2]
    percentage_complex_words = (len(complex_words) / len(words)) * 100
    
    # Calculate Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    return avg_sentence_length, percentage_complex_words, fog_index

def count_personal_pronouns(text):
    personal_pronouns = ["i", "we", "my", "ours", "us"]
    # Exclude "US" from personal pronouns
    text = re.sub(r'\bUS\b', '', text, flags=re.IGNORECASE)
    pronoun_counts = Counter(re.findall(r'\b(?:' + '|'.join(personal_pronouns) + r')\b', text.lower()))
    
    return pronoun_counts

def calculate_average_word_length(text):
    words = clean_text(text)
    total_characters = sum(len(word) for word in words)
    average_word_length = total_characters / len(words)
    
    return average_word_length

# Example usage:
text = "Your sample text goes here."
positive_words = set(["positive", "good", "great"])  # Example positive words
negative_words = set(["negative", "bad", "awful"])  # Example negative words

positive_score, negative_score, polarity_score, subjectivity_score = calculate_sentiment(text, positive_words, negative_words)
print("Positive Score:", positive_score)
print("Negative Score:", negative_score)
print("Polarity Score:", polarity_score)
print("Subjectivity Score:", subjectivity_score)

avg_sentence_length, percentage_complex_words, fog_index = analyze_readability(text)
print("Average Sentence Length:", avg_sentence_length)
print("Percentage of Complex Words:", percentage_complex_words)
print("Fog Index:", fog_index)

pronoun_counts = count_personal_pronouns(text)
print("Personal Pronoun Counts:", pronoun_counts)

average_word_length = calculate_average_word_length(text)
print("Average Word Length:", average_word_length)


# In[ ]:




