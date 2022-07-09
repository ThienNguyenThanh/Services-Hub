
import json

import nltk
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
    print(en_input.lower())

    # Tokenize the input
    input_text = word_tokenize(en_input.lower())
    pos_result = nltk.pos_tag(input_text)

    print(pos_result)

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
    print(f'user input: {user_input["noun"]}')

    result = []
    # result.append(user_input["noun"])
    for verb in user_input["verb"]:
        verbs_synonyms = []
        for syn in wordnet.synsets(verb, pos=wordnet.VERB):

            # Not add existed synonym in verbs_synonyms list
            [verbs_synonyms.append(i.name()) for i in syn.lemmas() if i.name() not in verbs_synonyms]
        result.append({'verb': verb, 'synonyms': verbs_synonyms, 'noun':user_input["noun"]})
    
    return result

def identify_category(list_verbs_syns: list, category_file: json):
    pass
        


if __name__ == "__main__":
    
    # text = word_tokenize("order pizza")
    # for i in text:
    # print(nltk.pos_tag(text))
    # print(lesk(text, "purchase"))

    
    

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
                        "movie tickets":"movie ticket"
                    },
                    "travel": {
                        "plane_ticket": "plane ticket",
                        "bus ticket": "bus ticket",
                        "book_hotel": "book hotel",
                    }
    }
    
    result = search_verbs_synonym("mua vé xem phim")
    print(result)

    # possible_category = []
    # for key, value in CATEGORY.items():
    #     if value in list_nouns:
    #         possible_category.append(key)
            

    


    # list_syn = syns[0]["synonyms"]

    # keys = CATEGORY.keys()
    # result  = {}
    # for syn in list_syn:
    #     if syn in keys:
    #         result[syn] = CATEGORY[syn]
    #         break
    # print(result)

        
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


