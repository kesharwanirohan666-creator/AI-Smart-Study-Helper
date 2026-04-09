import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download necessary NLTK data
def download_nltk_resources():
    """Downloads NLTK resources required for processing."""
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('averaged_perceptron_tagger_eng', quiet=True)
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

def summarize_text(text, num_sentences=3):
    """
    Summarizes the given text using a frequency-based approach.
    1. Tokenize sentences and words.
    2. Calculate word frequencies (excluding stopwords and punctuation).
    3. Score sentences based on word frequencies.
    4. Select top sentences.
    """
    if not text.strip():
        return "Text is too short to summarize."

    # Tokenize into sentences
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text

    # Tokenize into words and clean
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    punch = set(string.punctuation)
    
    word_freq = {}
    for word in words:
        if word not in stop_words and word not in punch:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Normalize frequency
    if not word_freq:
        return text

    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq

    # Score sentences
    sent_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sent_scores[sent] = sent_scores.get(sent, 0) + word_freq[word]

    # Get top sentences
    summarized_sentences = sorted(sent_scores, key=sent_scores.get, reverse=True)[:num_sentences]
    return " ".join(summarized_sentences)

def generate_questions(text):
    """
    Generates basic study questions from the text by identifying 
    important nouns using POS tagging.
    """
    if not text.strip():
        return ["Add more content to generate questions."]

    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)
    
    # Extract Nouns (NN, NNP)
    nouns = [word for word, pos in tagged if pos in ('NN', 'NNP') and len(word) > 3]
    unique_nouns = list(set(nouns))

    if not unique_nouns:
        return ["Could not find enough keywords to generate questions."]

    questions = []
    # Limit to 5 questions
    for noun in unique_nouns[:5]:
        questions.append(f"What is the significance of '{noun}' in this context?")
        questions.append(f"Can you explain '{noun}' in your own words?")
    
    return questions[:5]

# Ensure resources are available on import
download_nltk_resources()
