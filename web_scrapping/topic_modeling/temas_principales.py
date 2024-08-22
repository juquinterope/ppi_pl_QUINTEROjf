import nltk # type:ignore
from nltk.corpus import stopwords # type:ignore
from nltk.stem import SnowballStemmer # type:ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type:ignore
from gensim import corpora, models # type:ignore
from wordcloud import WordCloud # type:ignore
import matplotlib.pyplot as plt # type:ignore
from news_titles import titulos_noticias


titulos = titulos_noticias()