import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
import io

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

with io.open('articleText.txt', encoding ="utf-8") as f:
	doc_complete = f.read().splitlines()
# print doc_complete

#cleaning the data present(removing non-ascii characters, links, etc)
for i, line in enumerate(doc_complete):
	doc_complete[i] = re.sub(r'http\S+', '', doc_complete[i])
	doc_complete[i] = re.sub('[^A-Za-z0-9]+', ' ', doc_complete[i])

# print doc_complete[0]

# cleaning and preprocessing of the docs
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]  

# creating a term dictionary of our corpus, where each and every unique term is asignes an index
dictionary = corpora.Dictionary(doc_clean)

# converting list of docs to term-word matrix.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# creation and the running of the model on the created matrix
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=20, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=20, num_words=10))