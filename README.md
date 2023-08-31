# Issue Classification example

In this example we perform a logical regression on a dataset of github issues to predict the labels on newly entered tickets.

The data is gathered from the quarkusio/quarkus repository, which provides a dataset that includes title and body (of the issues reported) and is labeled using labels (i.e. area/devmode, or kind/bug).

The idea is to develop a regression model from this that can infer the label(s) for newly entered issues.
