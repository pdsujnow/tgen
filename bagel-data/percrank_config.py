#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sklearn.feature_extraction.dict_vectorizer import DictVectorizer
from sklearn.feature_selection.univariate_selection import SelectPercentile
from sklearn.linear_model.logistic import LogisticRegression


config = {
          'alpha': 0.1,
          'passes': 100,
          'rival_number': 10,
          'features': [
#                        'lemma-count: value tree t_lemma',
#                        'formeme-count: value tree formeme',
                       'lemma-present: presence tree t_lemma',
                       'formeme-present: presence tree formeme',
                       'lemma-dai: dai_cooc tree t_lemma',
                       'formeme-dai: dai_cooc tree formeme',
                       'depth: depth tree',
                       'max-children: max_children tree',
                       'nodes-per-dai: nodes_per_dai tree',
                       'rep-nodes-per-rep-dai: rep_nodes_per_rep_dai tree',
                       'rep-nodes: rep_nodes tree',
                       ],
          'rival_gen_strategy': ['gen_cur_weights'],  # ['other_inst', 'random'],
          }
