import spacy
import json

from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("country_text.txt", encoding="utf8") as f:
    TEXT = f.read()
    
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)

patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

doc = nlp(TEXT)
doc.ents = []

for match_id, start, end in matcher(doc):
    span = Span(doc, start, end, label="GPE")

    doc.ents = list(doc.ents) + [span]

    span_root_head = span.root.head
    print(span_root_head.text, "-->", span.text)

print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])