import pickle
import gensim

#model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  



#print model['cricket']

#sentence = ["London", "is", "the", "capital", "of", "Great", "Britain"]
#vectors = [model[w] for w in sentence]
#favorite_color = pickle.load(a1)
a1=open( 'objs.pickle', 'r' ) 
favorite_color = pickle.load(a1)

for line in favorite_color:
	print (line)
