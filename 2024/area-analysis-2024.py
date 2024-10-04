# ---
# title: 2024 VIS Area Curation Committee Area Analysis
# self-contained: true
# format:
#   html: 
#     code-fold: true
#     theme: simplex
#     toc: true
#     jupyter: python3
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Summary
#
# This report summarizes the findings, recommendations, and process by the VIS Area Curation Committee (ACC) regarding the areas used for paper submissions to IEEE VIS 2024.
# We use submission information from VIS 2024 to analyze the impact of the topics to the area model.
#
# **Given the information we have access to, the areas seem relatively balanced, and we do not make recommendations for any changes, creation or merging, at this time.**
#
# The full data and source code to rebuild this project are available [here](https://github.com/ieee-vgtc/ieeevis-area-curation-committee-reports).
#
# * Committee members 2024: Jean-Daniel Fekete (co-chair), Alexander Lex (co-chair), Helwig Hauser, Ingrid Hotz, David Laidlaw, Torsten Möller, Michael Papka, Danielle Szafir, Yingcai Wu.
#
# Last edited: 2024-10-04.

# +
# %load_ext autoreload
# %autoreload 2
def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True

IN_NOTEBOOK = in_notebook()
# -

min_df = 25
max_df = 0.1
max_words = 100000
vocab_sample = 250000
num_dims = 50
filt_min_score = 4
n_neighbors = 10
llm_family = "specter2"
# llm_family = "all-MiniLM-L6-v2"

import pandas as pd   # noqa
df = pd.read_csv('../data/papers_all.csv', index_col=None)
df.abstract = df.abstract.fillna('')
df.keywords = df.keywords.fillna('')
# print(df.columns)
# prints: Index(['abstract', 'title', 'keywords', 'Area', 'year'], dtype='object')
df['text'] = df.abstract + ' ' \
            + df.keywords + ' ' \
            + df.title
# df = df[["Year", "Title", "Abstract", "AuthorKeywords", "text"]]
docs = list(df.text)
# df.head()

# ## Highlights of Topic Analysis
# We pass the 2021-2024 abstract texts to the Bertopic library and it computes topics magically.
# These topics seem representative of the main trends in visualization during the period.

# +
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import MaximalMarginalRelevance
from umap import UMAP

vectorizer_model = CountVectorizer(ngram_range=(1, 3), stop_words="english")
representation_model = MaximalMarginalRelevance(diversity=0.3)

sentence_model = SentenceTransformer('sentence-transformers/allenai-specter')
embeddings = sentence_model.encode(docs, show_progress_bar=IN_NOTEBOOK)

topic_model = BERTopic(representation_model=representation_model)
topics, probs = topic_model.fit_transform(docs, embeddings)
topic_model.update_topics(docs, vectorizer_model=vectorizer_model)

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', 1000, 'display.width', 200):
    print(topic_model.get_topic_info()[["Topic", "Count", "Representation"]])
# df_model_last = topic_model.get_topic_info()
# df_model_last.to_csv("topics-all.csv", index=False)

# +
from scipy.cluster import hierarchy as sch
import numpy as np

linkage_function = lambda x: sch.linkage(x, 'ward', optimal_ordering=True)
hierarchical_topics = topic_model.hierarchical_topics(docs, linkage_function=linkage_function)

topic_model.visualize_hierarchy(hierarchical_topics=hierarchical_topics) 
# -

# ## Visualization of the Topic Map
# These topics can be visualized over a map.
#

if IN_NOTEBOOK:
    reduced_embeddings = UMAP(n_neighbors=10, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    vis = topic_model.visualize_documents(df.title, reduced_embeddings=reduced_embeddings, hide_annotations=True, title='<b>Documents and Topics 2021-2024</b>')
    # vis.write_html("topics-all.html")
else:
    vis = None
vis


# ## Analysis of the Areas
#
# To find out if some topics are over- or under-represented, we visualize the topics per Area.
# The largest area, "Application", contains a relatively balanced mix of topics; there is no clear thematic way of splitting it.

topics_per_class = topic_model.topics_per_class(docs, classes=list(df.Area))
fig = topic_model.visualize_topics_per_class(topics_per_class, top_n_topics=10)
fig.for_each_trace(lambda bar : bar.update(visible=True))


