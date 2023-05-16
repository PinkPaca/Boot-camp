import spacy

nlp = spacy.load('en_core_web_sm')

# language model
sample = "The quick brown fox, jumps over the lazy dog."
# print(sample.split()) # how string system sees the sentence

doc = nlp(sample)

# how spacy sees the sentence
# print([token.orth_ for token in doc])
