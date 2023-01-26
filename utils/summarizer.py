import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from heapq import nlargest

def summarizer(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)    
    tokens = [token.text for token in doc]
    punctuation = string.punctuation + '\n'

    word_frequencies = {}
    max_val = 0
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
                max_val = max(max_val, word_frequencies[word.text])
    max_frequency = max_val 

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    score = {}
    key = {}
    for i, (sentence, sc) in enumerate(sentence_scores.items()):
        score[i] = sc
        key[i] = sentence
        i += 1

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, score, key = score.get)

    summary = sorted(summary)
    final_summary = [key[x].text for x in summary]
    final_summary = ' '.join(final_summary)

    return final_summary
