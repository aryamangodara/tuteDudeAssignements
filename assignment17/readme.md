# NLP Text Preprocessing Pipeline

A complete step-by-step Natural Language Processing (NLP) text preprocessing project covering basic to advanced techniques.

## 📋 Project Overview

This project demonstrates the entire NLP text cleaning and preprocessing pipeline as per the assigned tasks. It includes basic cleaning, advanced noise removal, stopword handling, tokenization, stemming, lemmatization, and a final unified preprocessing function.

## ✅ Completed Tasks

### Task 1-2: Basic Text Cleaning
- Converted text to lowercase
- Removed punctuation and numbers
- Removed extra whitespaces
- Created `clean_text_basic` column

### Task 3: Removing Noise (Advanced Cleaning)
- Removed URLs
- Removed email addresses
- Removed HTML tags
- Removed special characters & emojis
- Created `clean_text_advanced` column

### Task 4: Handling Stopwords
- Loaded English stopwords using NLTK
- Removed stopwords from cleaned text
- Created `text_no_stopwords` column

### Task 5: Handling Repeated Characters & Slang (Optional)
- Normalized repeated characters (e.g., `soooo` → `so`)
- Created a small slang dictionary and replaced slang terms

### Task 6: Tokenization
- Performed **Word Tokenization**
- Performed **Sentence Tokenization**
- Displayed tokens for multiple text samples

### Task 7: Stemming
- Applied **Porter Stemmer**
- Compared original words vs stemmed words

### Task 8: Lemmatization
- Applied **WordNet Lemmatizer**
- Compared stemming vs lemmatization results

### Task 9: Final NLP Pipeline
- Created a single function `nlp_preprocess(text)`
- Performed: Lowercasing → Noise Removal → Stopword Removal → Tokenization → Lemmatization
- Final output stored in `final_clean_text` column

### Task 10: Observations & Insights
- Difference between basic and advanced cleaning
- Why lemmatization is preferred over stemming
- Importance of preprocessing in NLP models

## 🛠 Technologies Used

- Python
- pandas
- NLTK (Natural Language Toolkit)
- Regular Expressions (re)

## 📁 Files Structure
