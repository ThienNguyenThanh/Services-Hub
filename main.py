import json
import time
from nis import cat
from sre_constants import CATEGORY
from unicodedata import category

import nltk
import spacy
from attr import s
from nltk.corpus import verbnet, wordnet
from nltk.wsd import lesk

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
        for syn in wordnet.synsets(verb, pos=wordnet.NOUN):

            # Not add existed synonym in verbs_synonyms list
            [verbs_synonyms.append(i.name()) for i in syn.lemmas() if i.name() not in verbs_synonyms]
        result.append({'verb': verb, 'synonyms': verbs_synonyms})

    return result
        


if __name__ == "__main__":
    start = time.time()
    CATEGORY =  {   
                    "payment": {
                        "electricity": "electricity",
                        "water": "water",
                        "loan": "loan",
                        "phone_card": "phone card",
                        "phone_data": "phone data"
                    },
                    "finance": {
                        "investment": "investment",
                        "trade": "trade",
                        "loan": "loan"
                    },
                    "cuisine": {
                        "food": "order food"
                    },
                    "shopping": {
                        "cloth": "cloth",
                        "technology": "technology",
                        "pet": "pet"
                    },
                    "medical": {
                        "medicine": "medicine"
                    },
                    "insurance": {
                        "health_insurance": "health insurance",
                        "car_insurance": "car insurance",
                        "bike_insurance": "bike insurance"
                    },
                    "entertainment": {
                        "movie_ticket":"movie ticket"
                    },
                    "travel": {
                        "plane_ticket": "plane ticket",
                        "bus ticket": "bus ticket",
                        "book_hotel": "book hotel",
                    }
    }
    syns = search_synonym("travel Dallas")
    list_syn = syns[0]["synonyms"]

    keys = CATEGORY.keys()
    result  = {}
    for syn in list_syn:
        if syn in keys:
            result[syn] = CATEGORY[syn]
            break
    print(result)
    print(f"Total time: {time.time() - start}")
        
    # for syn in wordnet.synsets("travel"):
    #     for i in syn.lemmas():
    #         print(i.name())
   
    # print(lesk(['travel','Dallas'], 'travel'))
    # print(wordnet.synset('travel.v.06').definition())

    # {   
    #                 "thanh toán": {
    #                     "điện": "điện",
    #                     "nước": "nước",
    #                     "vay": "vay",
    #                     "điện thoại": "điện thoại",
    #                     "dữ liệu": "dữ liệu"
    #                 },
    #                 "tài chính": {
    #                     "đầu tư": "đầu tư",
    #                     "trade": "trade",
    #                     "vay": "vay"
    #                 },
    #                 "ẩm thực": {
    #                     "món ăn": "đặt món ăn"
    #                 },
    #                 "mua sắm": {
    #                     "quần áo": "quần áo",
    #                     "điện tử": "điện tử",
    #                     "thú cưng": "thú cưng"
    #                 },
    #                 "y tế": {
    #                     "thuốc": "thuốc"
    #                 },
    #                 "bảo hiểm": {
    #                     "sức khoẻ": "sức khoẻ",
    #                     "ô tô": "ô tô",
    #                     "xe máy": "xe máy"
    #                 },
    #                 "giải trí": {
    #                     "xem phim":"vé xem phim"
    #                 },
    #                 "du lịch": {
    #                     "máy bay": "vé máy bay",
    #                     "xe khách": "vé xe khách",
    #                     "khách sạn": "đặt khách sạn",
    #                 }
    # }

    

    # print(category["payment"]["electricity"])


