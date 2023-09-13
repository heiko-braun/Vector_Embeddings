# Issue Classification example

In this example we perform a logical regression on a dataset of github issues to predict the labels on newly entered tickets.

The data is gathered from the `quarkusio/quarkus` repository, which provides a dataset that includes `title` and `body` (of the issues reported) and is labeled using labels (i.e. `area/devmode`, or `kind/bug`).

The idea is to develop a regression model from this that can infer the label(s) for newly entered issues.

## How to use this repo

The code is broken down into several Jupyter notebooks that need to be used in order:

1. [data_aquisition.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/data_aquisition.ipynb)
2. [embeddings.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/embeddings.ipynb)
3. [query.ipynb](https://github.com/heiko-braun/issue_classification/blob/main/notebooks/query.ipynb)