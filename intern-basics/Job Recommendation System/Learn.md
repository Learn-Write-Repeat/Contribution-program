# TfidfTransformer

*(sklearn.feature_extraction.text.TfidfVectorizer)*

It Converts a collection of raw documents to a matrix of TF-IDF features.
It is Equivalent to *CountVectorizer* followed by *TfidfTransformer*.
* CountVectorizer implements both tokenization and occurrence counting in a single class.
* TfidfTransformer helps in removing the stop words (e.g. “the”, “a”, “is” in English) which carry very little information about the actual contents of the document.

Tf means **term-frequency** while tf–idf means term-frequency times **inverse document-frequency**: tf-idf(t,d)=tf(t,d)\*idf(t).

Using the `TfidfTransformer`’s default settings, `TfidfTransformer(norm='l2', use_idf=True, smooth_idf=True, sublinear_tf=False)` the term frequency, the number of times a term occurs in a given document, is multiplied with idf component, which is computed as

### idf(t) = log((1+n)/1+df(t)) +1

where n is the total number of documents in the document set, and df(t) is the number of documents in the document set that contain the term t. The resulting tf-idf vectors are then normalized by the Euclidean norm.

# cosine_similarity

*sklearn.metrics.pairwise.cosine_similarity(X, Y=None, dense_output=True)*

Compute cosine similarity between samples in X and Y.

Cosine similarity, or the cosine kernel, computes similarity as the normalized dot product of X and Y:

![cosine similarity](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d94e5903f7936d3c131e040ef2c51b473dd071d)

On L2-normalized data, this function is equivalent to linear_kernel.

![cosine image](https://www.oreilly.com/library/view/statistics-for-machine/9781788295758/assets/2b4a7a82-ad4c-4b2a-b808-e423a334de6f.png)
