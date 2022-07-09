import json

from flask import Flask

# from main1 import search_synonym

app = Flask(__name__)

@app.route('/category', methods=['GET'])
def get_users():
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

    # syns = search_synonym(querry)
    # list_syn = syns[0]["synonyms"]

    # keys = CATEGORY.keys()
    # result  = {}
    # for syn in list_syn:
    #     if syn in keys:
    #         result[syn] = CATEGORY[syn]
    #         break
    # return result

    return {}

    # return json.dumps(category[cate])
    

if __name__ == '__main__':
    app.run(debug=True)
