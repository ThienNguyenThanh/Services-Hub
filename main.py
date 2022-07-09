import json

from flask import Flask

from main1 import search_synonym

app = Flask(__name__)

CATEGORY =  json.load("category.json")

@app.route('/<string:querry>/', methods=['GET'])
def get_users(querry):
    

    # syns = search_synonym(querry)
    # list_syn = syns[0]["synonyms"]

    # keys = CATEGORY.keys()
    # result  = {}
    # for syn in list_syn:
    #     if syn in keys:
    #         result[syn] = CATEGORY[syn]
    #         break
    # return result
    syns = search_synonym(querry)
    # print(syns)

    return CATEGORY



    # return json.dumps(category[cate])
    

if __name__ == '__main__':
    app.run(debug=True)
