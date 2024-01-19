import spacy
from sklearn.metrics.pairwise import cosine_similarity

def get_colm(question, columns):
    nlp = spacy.load('en_core_web_sm')

    tokens = [token.lemma_ for token in nlp(question) if not token.is_stop and not token.is_punct]

    max_similarities = []
    for token in tokens:
        token_vector = nlp(token).vector
        column_vectors = [nlp(column).vector for column in columns]
        similarities = cosine_similarity([token_vector], column_vectors).flatten()
        max_similarity_index = similarities.argmax()
        max_similarities.append(similarities[max_similarity_index])

    max_similarity_index = max_similarities.index(max(max_similarities))
    identified_column = columns[max_similarity_index]

    # print("Identified Column:", identified_column)
    # print("Lemmatized Tokens:", tokens)
    # print("Max Similarities:", max_similarities)

    return identified_column


# Example usage
# question = "Which city has my best sales?"
# columns = ['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER', 'SALES',
#            'ORDERDATE', 'STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID', 'PRODUCTLINE',
#            'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE', 'ADDRESSLINE1', 'ADDRESSLINE2',
#            'CITY', 'STATE', 'POSTALCODE', 'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME',
#            'CONTACTFIRSTNAME', 'DEALSIZE']

# get_colm(question, columns)
