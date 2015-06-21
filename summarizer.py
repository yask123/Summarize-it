import math

import networkx as nx
import numpy as np

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def textrank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    return sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    # sentence_array = sentence_array[:math.floor(len(sentence_array) * 0.5)]
    
    # sentence_array = [s for i, s in sentence_array]
    
    # ret_string = ""
    # for i in range(len(sentence_array)):
    #     ret_string += sentence_array[i]
    #     ret_string += " "

    # return str(ret_string)
