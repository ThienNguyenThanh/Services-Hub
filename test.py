import json

import spacy

nlp = spacy.load("en_core_web_lg")

def analysis_input(input: str)->json:
    """Extract all verbs, nouns and proper nouns in user's input"""

    # Tokenize the input
    doc = nlp(input)

    list_verb = [token.lemma_ for token in doc if token.pos_ == 'VERB']             # Get list of verbs in user's input
    list_prop_noun = [token.text for token in doc if token.pos_ == 'PROPN']         # Get list of proper nouns in user's input
    list_noun = [token.text for token in doc if token.pos_ == 'NOUN']               # Get list of nouns in user's input

    out_put = json.dumps({
                        'verb': list_verb, 
                        'proper_noun': list_prop_noun,
                        'noun': list_noun
    })

    return out_put


# verb = analysis_input("travel Texas, eat chicken")
a = nlp('travel')
b = nlp('trip')
print(f'{a.similarity(b)}')
# doc = nlp("Travel Texas")
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
