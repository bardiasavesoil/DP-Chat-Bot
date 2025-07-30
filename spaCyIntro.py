# import spacy

# nlp = spacy.blank("en")

# doc = nlp("Hello World!")

# # for token in doc:
# #     print(token.text)

# # token = doc[1]
# # print(token.text)

# span = doc[1:3]
# print(span.text)

# doc = nlp("It costs $5.")

# print("Index: ", [token.i for token in doc])
# print("Text: ", [token.text for token in doc])

# print("is_alpha: ", [token.is_alpha for token in doc])
# print("is_punct: ", [token.is_punct for token in doc])
# print("like_num: ", [token.like_num for token in doc])

# nlp = spacy.load("en_core_web_sm")

# doc = nlp("She ate the pizza")

# # for token in doc:
# #     print(token.text, token.pos_)

# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.head.text)

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# print(spacy.explain("GPE"))
# print(spacy.explain("NNP"))
# print(spacy.explain("dobj"))

# from spacy.matcher import Matcher

# nlp = spacy.load("en_core_web_sm")

# matcher = Matcher(nlp.vocab)

# pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
# matcher.add("IPHONE_PATTERN", [pattern])

# doc = nlp("Upcoming iPhone X release date leaked")

# matches = matcher(doc)

# for match_id, start, end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text)

# pattern = [
#     {"IS_DIGIT": True},
#     {"LOWER": "fifa"},
#     {"LOWER": "world"},
#     {"LOWER": "cup"},
#     {"IS_PUNCT": True}
# ] 

# doc = nlp("2018 FIFA World Cup: France won!")

# matcher.add("FIFA_PATTERN", [pattern])
# matches = matcher(doc)

# for match_id, start, end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text)

# pattern = [
#     {"LEMMA": "love", "POS": "VERB"},
#     {"POS": "NOUN"}
# ]

# doc = nlp("I loved dogs but now I love cats more.")

# matcher.add("LOVED_PATTERN", [pattern])

# matches = matcher(doc)

# for match_id, start, end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text)



# pattern = [
#     {"LEMMA": "buy"},
#     {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
#     {"POS": "NOUN"}
# ]

# doc = nlp("I bought a smartphone. Now I'm buying apps.")

# matcher.add("BUY_PATTERN", [pattern])

# matches = matcher(doc)


# for match_id, start, end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text)

# Imports the library
import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Pattern to match 
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]
# add the pattern to the matcher
matcher.add("BUY_PATTERN", [pattern])

# Process some text
doc = nlp("I bought a smartphone. Now I'm buying apps.")

# Call the matcher on the doc
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

