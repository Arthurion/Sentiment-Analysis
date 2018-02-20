# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:13:42 2018

@author: Arthurion9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean

data_train = pd.read_csv('amazon_reviews/train.csv', names=['rating','title','review'])
data_test = pd.read_csv('amazon_reviews/test.csv', names=['rating','title','review'])

data_train['title'] = [str(x) for x in data_train['title']]
data_test['title'] = [str(x) for x in data_test['title']]
data_train['len_title'] = [len(x) for x in data_train['title']]
data_test['len_title'] = [len(x) for x in data_test['title']]



### Barplots of mean length title and text for each score. ###

# Title
five_stars_title = data_train['title'][data_train['rating'] == 5]
four_stars_title = data_train['title'][data_train['rating'] == 4]
three_stars_title = data_train['title'][data_train['rating'] == 3]
two_stars_title = data_train['title'][data_train['rating'] == 2]
one_star_title = data_train['title'][data_train['rating'] == 1]

mean_title = [0] * 5
mean_title[4] = mean([len(x) for x in five_stars_title])
mean_title[3] = mean([len(x) for x in four_stars_title])
mean_title[2] = mean([len(x) for x in three_stars_title])
mean_title[1] = mean([len(x) for x in two_stars_title])
mean_title[0] = mean([len(x) for x in one_star_title])

fig, ax = plt.subplots()
ax.bar(range(1,6), mean_title)
ax.set_xlabel('Rating')
ax.set_ylabel('Mean length of titles')
ax.set_title('Mean length of titles according to the rating.')
plt.show()


# Text review
five_stars_review = data_train['review'][data_train['rating'] == 5]
four_stars_review = data_train['review'][data_train['rating'] == 4]
three_stars_review = data_train['review'][data_train['rating'] == 3]
two_stars_review = data_train['review'][data_train['rating'] == 2]
one_star_review = data_train['review'][data_train['rating'] == 1]

mean_review = [0] * 5
mean_review[4] = mean([len(x) for x in five_stars_review])
mean_review[3] = mean([len(x) for x in four_stars_review])
mean_review[2] = mean([len(x) for x in three_stars_review])
mean_review[1] = mean([len(x) for x in two_stars_review])
mean_review[0] = mean([len(x) for x in one_star_review])

fig, ax = plt.subplots()
ax.bar(range(1,6), mean_review)
ax.set_xlabel('Rating')
ax.set_ylabel('Mean length of text reviews')
ax.set_title('Mean length of text reviews according to the rating.')
plt.show()



### Barplots of mean number of words of title and text for each score. ###

# Title
five_stars_title = data_train['title'][data_train['rating'] == 5]
four_stars_title = data_train['title'][data_train['rating'] == 4]
three_stars_title = data_train['title'][data_train['rating'] == 3]
two_stars_title = data_train['title'][data_train['rating'] == 2]
one_star_title = data_train['title'][data_train['rating'] == 1]

mean_title = [0] * 5
mean_title[4] = mean([len(x.split()) for x in five_stars_title])
mean_title[3] = mean([len(x.split()) for x in four_stars_title])
mean_title[2] = mean([len(x.split()) for x in three_stars_title])
mean_title[1] = mean([len(x.split()) for x in two_stars_title])
mean_title[0] = mean([len(x.split()) for x in one_star_title])

fig, ax = plt.subplots()
ax.bar(range(1,6), mean_title)
ax.set_xlabel('Rating')
ax.set_ylabel('Mean number of words of titles')
ax.set_title('Mean number of words of titles according to the rating.')
plt.show()


# Text review
five_stars_review = data_train['review'][data_train['rating'] == 5]
four_stars_review = data_train['review'][data_train['rating'] == 4]
three_stars_review = data_train['review'][data_train['rating'] == 3]
two_stars_review = data_train['review'][data_train['rating'] == 2]
one_star_review = data_train['review'][data_train['rating'] == 1]

mean_review = [0] * 5
mean_review[4] = mean([len(x.split()) for x in five_stars_review])
mean_review[3] = mean([len(x.split()) for x in four_stars_review])
mean_review[2] = mean([len(x.split()) for x in three_stars_review])
mean_review[1] = mean([len(x.split()) for x in two_stars_review])
mean_review[0] = mean([len(x.split()) for x in one_star_review])

fig, ax = plt.subplots()
ax.bar(range(1,6), mean_review)
ax.set_xlabel('Rating')
ax.set_ylabel('Mean number of words of text reviews')
ax.set_title('Mean number of words of text reviews according to the rating.')
plt.show()




### N-grams ###
from nltk import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print(grams)