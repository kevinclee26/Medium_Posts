#!/usr/bin/env python
# coding: utf-8

# In[1]:


sample_text="A huge trash-collecting system designed to clean up plastic floating in the Pacific Ocean is finally picking up plastic, its inventor announced Wednesday."


# In[2]:


import unidecode
sample_text=sample_text.lower()
sample_text=unidecode.unidecode(sample_text)


# In[3]:


import re, string
sample_text=re.sub(r'\d+', '', sample_text)
sample_text=sample_text.translate(str.maketrans('', '', string.punctuation))


# In[4]:


sample_text=sample_text.strip()


# In[5]:


import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp(sample_text)
tokens=[token for token in doc]
first_sentence=list(doc.sents)[0]


# In[6]:


spacy_stop_words=spacy.lang.en.stop_words.STOP_WORDS
spacy_stop_words
filtered_tokens=[token for token in tokens if not token.is_stop]


# In[7]:


lemmas=[token.lemma_ for token in filtered_tokens]


# In[8]:


pos=[token.pos_ for token in filtered_tokens]


# In[9]:


entities=[(entity, entity.label_) for entity in doc.ents]


# In[10]:


noun_chunks=[noun for noun in doc.noun_chunks]


# In[11]:


dependencies=[(token, token.dep_) for token in filtered_tokens]


# In[12]:


from pathlib import Path
import os
svg=spacy.displacy.render(first_sentence, style="dep", jupyter=False, options={'distance':100})
output_path=Path(os.getcwd()+'/first_sentence.svg')
output_path.open("w", encoding="utf-8").write(svg)


# In[13]:


import pandas as pd
first_sentence_df=pd.DataFrame()
first_sentence_df['tokens']=tokens
first_sentence_df['text']=first_sentence_df['tokens'].map(lambda x: x.text)
first_sentence_df['lemma']=first_sentence_df['tokens'].map(lambda x: x.lemma_)
first_sentence_df['pos']=first_sentence_df['tokens'].map(lambda x: x.pos_)
first_sentence_df['dep']=first_sentence_df['tokens'].map(lambda x: x.dep_)
first_sentence_df['is_stop']=first_sentence_df['tokens'].map(lambda x: x.is_stop)


# In[14]:


first_sentence_df[['text', 'lemma', 'pos', 'dep', 'is_stop']]

