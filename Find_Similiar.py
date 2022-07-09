import gensim.models as models
from gensim.models import KeyedVectors, Word2Vec 
path = "./Vecto/wiki.vi.model.bin"
word2vec_model = KeyedVectors.load_word2vec_format(path, binary=True)


