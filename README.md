# Issue Classification example

In this example we perform text similarity search over a set of github issues to predict the labels on newly entered tickets.

The data is gathered from the `quarkusio/quarkus` repository, which provides a dataset that includes `title` and `body` (of the issues reported) and is labeled using labels (i.e. `area/devmode`, or `kind/bug`).

[sbert sentence transformers](https://www.sbert.net) are used to compute the embeddings, which are stored in a vector database ([qdrant](https://qdrant.tech) in our case). 

## How to use this repo

The code is broken down into several Jupyter notebooks that need to be used in order:

1. [data_aquisition.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/data_aquisition.ipynb)
2. [embeddings.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/embeddings.ipynb)
3. [query.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/query.ipynb)
