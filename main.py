import json

import spacy
from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_lg")

def analysis_input(input: str)-> dict:
    """Extract all verbs, nouns and proper nouns in user's input"""

    # Tokenize the input
    doc = nlp(input)

    list_verb = [token.lemma_ for token in doc if token.pos_ == 'VERB']             # Get list of verbs in user's input
    list_prop_noun = [token.text for token in doc if token.pos_ == 'PROPN']         # Get list of proper nouns in user's input
    list_noun = [token.text for token in doc if token.pos_ == 'NOUN']               # Get list of nouns in user's input

    out_put = {
                        'verb': list_verb, 
                        'proper_noun': list_prop_noun,
                        'noun': list_noun
    }

    return out_put


def search_synonym(search_querry: str) -> list:
    """Return a list of synonyms of each verb in user's input"""

    user_input = analysis_input(search_querry)

    result = []
    for verb in user_input["verb"]:
        verbs_synonyms = []
        for syn in wordnet.synsets(verb):

            # Not add existed synonym in verbs_synonyms list
            [verbs_synonyms.append(i.name()) for i in syn.lemmas() if i.name() not in verbs_synonyms]
        result.append({'verb': verb, 'synonyms': verbs_synonyms})

    return result
        


if __name__ == "__main__":
    syns = search_synonym("travel Dallas, eat fried chicken")
    print(syns)
    
   


