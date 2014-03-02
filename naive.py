import nltk.data
import nltk


pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]
neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')
              ]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


test_tweets = [(['feel', 'happy', 'this', 'morning'], 'positive'),
               (['larry', 'friend'], 'positive'),
               (['not', 'like', 'that', 'man'], 'negative'),
               (['house', 'not', 'great'], 'negative'),
               (['your', 'song', 'annoying'], 'negative')]



def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)


file = open('output1.txt', 'r')
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
text = file.read()
text1 = "I am not happy today because there is no rain"

for iter in sent_detector.tokenize(text.strip()):
    print iter
    print classifier.classify(extract_features(iter.split()))
