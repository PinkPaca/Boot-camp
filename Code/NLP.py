import spacy

nlp = spacy.load('en_core_web_sm')

# language model
sample = "The quick brown fox, jumps over the lazy dog."
# print(sample.split()) # how string system sees the sentence

doc = nlp(sample)

# how spacy sees the sentence
# print([token.orth_ for token in doc])

# leaving out the underscore gives the integer code of the word
# print([(token, token.orth_, token.orth) for token in doc])

# words that spacy thinks are stop words: insignificant
'''for word in doc:
    if word.is_stop == True:
        print(word) '''

# Lemmatisation gives the origin word
sample = "sing sang singing"
doc = nlp(sample)

print([token.lemma_ for token in doc])

# Entity Recognition
wiki_priyanka = """Priyanka Chopra Jonas (pronounced [pɾɪˈjəŋka ˈtʃoːpɽa]) (born 18 July 1982)[1] is an Indian actress and producer. The winner of the Miss World 2000 pageant, Chopra is one of India's highest-paid actresses and has received numerous accolades, including two National Film Awards and five Filmfare Awards. In 2016, the Government of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world. In the next two years, Forbes listed her among the World's 100 Most Powerful Women, and in 2022, she was named in the BBC 100 Women list."""

nlp_priyanka = nlp(wiki_priyanka)
# print([(i, i.label_, i.label) for i in nlp_priyanka.ents])
# ents is entity regonition

entity_fac = spacy.explain("CARDINAL")
print(f"FAC:{entity_fac}")
