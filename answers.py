import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_answer(df, question, column):

    nlp = spacy.load('en_core_web_sm')

    tokens = [token.lemma_ for token in nlp(question) if not token.is_stop and not token.is_punct]

    processed_question = ' '.join(tokens)

    vectorizer = TfidfVectorizer()
    productline_vectors = vectorizer.fit_transform(df[column].astype(str).fillna(''))

    question_vectors = vectorizer.transform([processed_question])

    similarity = cosine_similarity(question_vectors, productline_vectors).flatten()

    index_max_similarity = similarity.argmax()

    answer = df.loc[index_max_similarity]

    return answer
