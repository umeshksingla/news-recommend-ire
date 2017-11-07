import re,os
import json
import ast,nltk
import datetime
from stemming.porter2 import stem
from collections import defaultdict, Counter
from string import punctuation
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import logging
import numpy as np
import time
import operator
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from sklearn.preprocessing import Imputer
#from blagging import BlaggingClassifier
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn import model_selection, metrics,cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import class_weight
from sklearn.ensemble import RandomForestClassifier



training_data = []
# Articles that has category given
with open('articles.json','r') as data_file:
    line = data_file.readline()
    while line:
        line = ast.literal_eval(line)
        training_data.append(line)
        line = data_file.readline()
    # data_file.close()


testing_data = []
# Articles that has no category given
with open('articles_wo.json','r') as data_file:
    line = data_file.readline()
    while line:
        line = ast.literal_eval(line)
        testing_data.append(line)
        line = data_file.readline()
    # data_file.close()



# function to parse sentences to words and remove stopwords from sentence
def sentence_to_wordlist( sentence, remove_stopwords=True ):
    text = re.sub("[^a-zA-Z]"," ",sentence)
    words = text.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return(words)

# function to parse text to sentences using tokenizer mentioned above
def text_to_sentences(text,tokenizer,remove_stopwords=True):
    raw_sentences = tokenizer.tokenize(text.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append( sentence_to_wordlist( raw_sentence, \
              remove_stopwords ))
    return sentences

categories_dict = {'automobiles' : 1, 'business' : 2, 'computing' : 3, 'criminals' : 4, 'entertainment' : 5, 'fashion' : 6,\
                  'foods' : 7, 'health' : 8, 'lifestyle' : 9, 'pbusiness' : 10, 'pfashion' : 11, 'phealth' : 12,
                  'plifestyle' : 13, 'politics' : 14, 'ptechnology' : 15, 'ptravel' : 16, 'science' : 17, 'sports' : 18,
                  'technology' : 19, 'travel' : 20}

#words = []
classes = []
documents = []
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    #words.extend(nltk.word_tokenize(pattern['desc']))
    documents += [[stem(str(word)) for word in sentence] for sentence in [text_to_sentences(pattern['desc'], tokenizer)]]
    classes.append(categories_dict[pattern['category']])
    #if pattern['category'] not in no_classes:
    #    no_classes.append(pattern['category'])

for pattern in testing_data:
    documents += [[stem(str(word)) for word in sentence] for sentence in [text_to_sentences(pattern['desc'],tokenizer)]]

def class_info(classes):
    counts = Counter(classes)
    total = sum(counts.values())
    #print counts
    counts = sorted(counts.items(), key=operator.itemgetter(1),reverse = True)
    for cls in counts:
        print "%6s : % 7d  =  %0.2f%%" %(cls[0],cls[1],float(cls[1])/total*100)
        
class_info(classes)
#print classes

print len(documents)

freq_classes = []
new_documents = []
for i in range(len(training_data)):
    freq_classes.append(classes[i])
    new_documents.append(documents[i])
    # if classes[i] not in [11,15,12,16]:
    #     if classes[i] == 13:
    #         freq_classes.append(11)
    #     elif classes[i] == 14:
    #         freq_classes.append(12)
    #     elif classes[i] == 17:
    #         freq_classes.append(13)
    #     elif classes[i] == 18:
    #         freq_classes.append(14)
    #     elif classes[i] == 19:
    #         freq_classes.append(15)
    #     elif classes[i] == 20:
    #         freq_classes.append(16)
    #     else:
for i in range(len(training_data),len(documents)):
    new_documents.append(documents[i])

print len(new_documents)
print len(freq_classes)


# Import the built-in logging module and configure it so that Word2Vec 
# creates nice output messages
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)

# Set values for various parameters
num_features = 100
# Word vector dimensionality                      
min_word_count = 2  # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 4           # Context window size                                                                                    
downsampling = 1e-5   # Downsample setting for frequent words
# Initialize and train the model (this will take some time)

print "Training model..."
model = Word2Vec(documents, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context)

# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=False)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
model_name = "100features_2minwords_4context"
model.save(model_name)
#model.save_word2vec_format(model_name,binary=False)


def makeFeatureVec(words,model,num_features):
    # Function to average all of the word vectors in a given
    # paragraph
    #
    # Pre-initialize an empty numpy array (for speed)
    featureVec = np.zeros((num_features,),dtype="float128")
    #
    nwords = 0.
    # 
    # Index2word is a list that contains the names of the words in 
    # the model's vocabulary. Convert it to a set, for speed 
    index2word_set = set(model.wv.index2word)
    #sorted_set = set(model.sort_vocab())
    #
    # Loop over each word in the review and, if it is in the model's
    # vocaublary, add its feature vector to the total
    for word in words:
        if word in index2word_set: 
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word])
    # 
    # Divide the result by the number of words to get the average
    featureVec = np.divide(featureVec,nwords)
    return featureVec

def getAvgFeatureVecs(reviews, model, num_features):
    # Given a set of reviews (each one a list of words), calculate 
    # the average feature vector for each one and return a 2D numpy array 
    # 
    # Initialize a counter
    counter = 0.
    # 
    # Preallocate a 2D numpy array, for speed
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float128")
    # 
    # Loop through the reviews
    for review in reviews:
    # Print a status message every 1000th review
        if counter%1000. == 0.:
            print "Review %d of %d" % (counter, len(reviews))

    # Call the function (defined above) that makes average feature vectors
        reviewFeatureVecs[int(counter)] = makeFeatureVec(review, model, \
           num_features)
    # Increment the counter
        counter = counter + 1.
    return reviewFeatureVecs


DataVecs = getAvgFeatureVecs( new_documents, model, num_features )
DataVecs = Imputer().fit_transform(DataVecs)


X_train = np.array(DataVecs[:10369])
X_test = np.array(DataVecs[10369:])
Y_train = np.array(freq_classes)

class_wt = class_weight.compute_class_weight('balanced', np.unique(Y_train), Y_train)
class_wt = dict(enumerate(class_wt.flatten(), 1))
print class_wt

# Decision tree algorithms often perform well on imbalanced datasets because their hierarchical structure allows them to learn signals from all thee respetive classes
# The tree ensembles (Random Forests, Gradient Boosted Trees, etc.) almost always outperform singular decision trees, so using random forest here.
clf=RandomForestClassifier()
# clf = DecisionTreeClassifier(min_samples_leaf=5,class_weight=class_wt)
train = clf.fit(X_train, Y_train)
predicted = model_selection.cross_val_predict(clf, X_train, Y_train, cv=5)
predict = train.predict(X_train)

print(metrics.accuracy_score(Y_train, predicted))
print(metrics.accuracy_score(Y_train, predict))
