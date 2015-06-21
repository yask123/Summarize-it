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
    sentence_array = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    sentence_array = np.asarray(sentence_array)
    
    fmax = float(sentence_array[0][0])
    fmin = float(sentence_array[len(sentence_array) - 1][0])
    
    temp_array = []
    # Normalization
    for i in range(0, len(sentence_array)):
        if fmax - fmin == 0:
        	temp_array.append(0)
        else:
        	temp_array.append((float(sentence_array[i][0]) - fmin) / (fmax - fmin))


    threshold = (sum(temp_array) / len(temp_array)) + 0.2
    
    sentence_list = []

    for i in range(0, len(temp_array)):
        if temp_array[i] > threshold:
            sentence_list.append(sentence_array[i][1])

    seq_list = []
    for sentence in sentence_array:
    	if sentence in sentence_list:
    		seq_list.append(sentence)
    
    return seq_list