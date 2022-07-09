
import json

import nltk

nltk.data.path.append('/Users/thien/nltk_data/')
from googletrans import Translator
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# from nltk.wsd import lesk

# nlp = spacy.load("en-core-web-lg")

def analysis_input(input: str)-> dict:
    """Extract all verbs, nouns and proper nouns in user's input"""

    translator = Translator()
    translation = translator.translate(input, dest='en')
    en_input = translation.text
    # print(en_input.lower())

    # Tokenize the input
    input_text = word_tokenize(en_input.lower())
    pos_result = nltk.pos_tag(input_text)

    # print(pos_result)

    # doc = nlp(input)

    # list_verb = [token.lemma_ for token in doc if token.pos_ == 'VERB']             # Get list of verbs in user's input
    # list_prop_noun = [token.text for token in doc if token.pos_ == 'PROPN']         # Get list of proper nouns in user's input
    # list_noun = [token.text for token in doc if token.pos_ == 'NOUN']               # Get list of nouns in user's input

    list_verbs, list_nouns = [], []
    for idx in range(len(pos_result)):
        if pos_result[idx][1] == 'NN' or pos_result[idx][1] == 'NNS':
            list_nouns.append(pos_result[idx][0])
        elif pos_result[idx][1] == 'VB' or pos_result[idx][1] == 'VBP':
            list_verbs.append(pos_result[idx][0])

    out_put = {
                        'verb': list_verbs,
                        'noun': list_nouns
    }

    return out_put


def search_verbs_synonym(search_querry: str) -> list:
    """Return a list of synonyms of each verb in user's input"""

    user_input = analysis_input(search_querry)


    result = []
    # result.append(user_input["noun"])
    for verb in user_input["verb"]:
        verbs_synonyms = []
        for syn in wordnet.synsets(verb, pos=wordnet.VERB):

            # Not add existed synonym in verbs_synonyms list
            [verbs_synonyms.append(i.name()) for i in syn.lemmas() if i.name() not in verbs_synonyms]
        result.append({'verb': verb, 'verbs_synonyms': verbs_synonyms, 'noun':user_input["noun"]})
    if len(user_input["verb"]) == 0:
        result.append({'noun':user_input["noun"]})

    
    return result

def identify_category(input_result: list, category_file: json):

    pass

        


if __name__ == "__main__":
    
    # text = word_tokenize("order pizza")
    # for i in text:
    # print(nltk.pos_tag(text))
    # print(lesk(text, "purchase"))

    
    

    CATEGORY =  {   
                    "payment": {
                        "electricity": {
                                            "description": "Thanh toán hoá đơn điện",
                                            "id": "urn:directory:app:83304571677442071"
                                        },
                        "water": "water",
                        "loan": "loan",
                        "phone card": "phone card",
                        "phone data": "phone data"
                    },
                    "finance": {
                        "investment": "investment",
                        "trade": "trade",
                        "loan": "loan"
                    },
                    "cuisine": {
                        "food": "order food"
                    },
                    "e-commerce": {
                        "clothes": "id of cloth",
                        "technology": "technology",
                        "pet": "pet"
                    },
                    "medical": {
                        "medicine": "medicine"
                    },
                    "insurance": {
                        "health insurance": "health insurance",
                        "car insurance": "car insurance",
                        "bike insurance": "bike insurance"
                    },
                    "entertainment": {
                        "movie tickets":"movie ticket"
                    },
                    "travel": {
                        "plane ticket": {
                        "description": "Thanh toán hoá đơn điện",
                        "id": "urn:directory:app:83304571677442071"},
                        "bus ticket": {
                        "description": "Thanh toán hoá đơn điện",
                        "id": "urn:directory:app:83304571677442071"},
                        "book hotel": {
                        "description": "Thanh toán hoá đơn điện",
                        "id": "urn:directory:app:83304571677442071"},
                    }
    }
    
    # querry = "mua quần áo"
    # result = search_verbs_synonym(querry)

    # if "verb" not in result[0]:
    #     re_querry = search_verbs_synonym("tôi " + querry)
    #     used_result = re_querry[0]
    # else:
    #     used_result = result[0]

    # print(f'used result: {used_result}')
    # possible_category = {}
    # for key, value in CATEGORY.items():
       
    #     if 'verb' in used_result and key in used_result['verb']:
    #         possible_category["key"] = key
    #     elif 'noun' in used_result:
    #         for noun in used_result['noun']:
    #             if possible_category:
    #                 break
    #             else:
    #                 for value in CATEGORY.values():
    #                     if noun in value and noun not in possible_category:
                            
    #                         possible_category["value"] = noun
                        
    #             # print(nn)
    #             # if noun in CATEGORY.values():

    # print(f'poss cate: {possible_category}')    

    # if "key" in possible_category:
    #     print(CATEGORY[possible_category["key"]])
    # else:
    #     for key, value in CATEGORY.items():
    #         if possible_category["value"] in value:
    #             print(CATEGORY[key][possible_category["value"]])
    
    


    wiki = TextBlob("")
    

