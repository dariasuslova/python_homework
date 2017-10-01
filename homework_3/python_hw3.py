
# coding: utf-8

# In[1]:


from pattern.web import Wikipedia, plaintext
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk import word_tokenize
from nltk.collocations import *
from collections import Counter, defaultdict
from itertools import islice, tee
import math
from nltk.corpus import stopwords


# In[6]:


class WikiParser:
    def __init__(self):
        pass
    def get_articles(self, start):
        list_of_strings = []
        article = Wikipedia().article(start)
        cleaned1 = article.plaintext()
        clean1 = re.sub(r'[,;:\(\)"\[\]<>\*\^\-]*', '', cleaned1)
        new1 = clean1.replace('  ', ' ')
        new1 = new1.lower()
        list_of_strings.append(new1)
        l = article.links
        for i in l:
            a = Wikipedia(language='en').article(i)
            if a is not None:
                cleaned = a.plaintext()
                clean = re.sub(r'[,;:\(\)"\[\]<>\*\^\-]*', '', cleaned)
                new = clean.replace('  ', ' ')
                new = new.lower()
                list_of_strings.append(new)
            
        return list_of_strings


# In[21]:


class TextStatistics:
    def __init___(self, articles):
        self.articles = articles
        pass
    def get_top_3grams(self, n, use_idf=False):
        d = defaultdict(int)
        a = self.articles
        sentences = []
        ar1 = []
        split_regex = re.compile(r'[.|!|?|…]')
        for i in a:
            sent = filter(lambda t: t, [t.strip() for t in split_regex.split(i)])
            sentences.append(sent)
            r1 = re.sub('[\.,!?;:\(\)"\[\]<>\*\^\-]*', '', i)
            ar1.append(r1)
        kolvo = len(sentences)
        ngrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(ar1, 3))))
        ngrams = [''.join(x) for x in ngrams]
        cntr = Counter(ngrams).most_common(n)
        for ngr in ngrams:
            for sent in sentences:
                if ngr in sent:
                    if d[ngr]<kolvo: 
                        d[ngr]+=1
        if use_idf == True:                
            res = []
            for nr, ch in cntr:
                for h, pred in d.items():
                    if nr == h:
                        res.append((nr, ch*math.log(kolvo/pred)))
            return (res)
        else:
            return(cntr)

    def get_top_words(self, n, use_idf=False):
        a1 = self.articles
        d1 = defaultdict(int)
        t1 = []
        tokens = []
        j1 = re.sub('[\.,!?;:\(\)"\[\]<>\*\^\-]*', '', a1)
        for i1 in t1:
            tok = word_tokenize(i1)
            tokens.append(tok)
        filtered_words = [word for word in tokens if word not in stopwords.words('english')]
        cnt = Counter(filtered_words).most_common(n)
        for w in filtered_words:
            for t in a1:
                if w in t:
                    if d1[w]<len(a1): 
                        d1[w]+=1
        if use_idf == True:                
            res1 = []
            for ws, c in cnt:
                for wrd, tx in d1.items():
                    print(ws, c)
                    print(wrd, tx)
                    if ws == wrd:
                        res1.append((ws, c*math.log(len(a1)/tx)))
            return (res1)
        else:
            return (cnt)


# In[119]:


t = Wikipedia().article('Hotels.com')
cleaned = t.plaintext()
cl = TextStatistics()
cl.articles = cleaned
print(cl.get_top_3grams(20))
print(cl.get_top_words(20, True))


# In[15]:


class Experiment:
    def __init__(self):
        pass
    def show_results(self):
        c = WikiParser()
        texts = c.get_articles("Natural language processing")
        cl = TextStatistics()
        cl.articles = texts
        n = cl.get_top_3grams(20)
        w = cl.get_top_words(20, True)
        return ('3grams 20 top:{} /n top 20 words {}'.format(n,w))
    


# In[22]:


cla = Experiment()
print(cla.show_results())

