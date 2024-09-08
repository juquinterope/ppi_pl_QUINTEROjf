import nltk # type:ignore
from nltk.corpus import stopwords # type:ignore
from nltk.stem import WordNetLemmatizer # type:ignore
from gensim import corpora, models # type:ignore
from wordcloud import WordCloud # type:ignore
import matplotlib.pyplot as plt # type:ignore
from itertools import chain
from news_titles import titulos_noticias


# Stopwords, es una coleccion de palabras conectoras por idiomas
nltk.download('stopwords')
# Recursos para la tokenizacion
nltk.download('punkt_tab')
# Recursos para la lematizacion
nltk.download('wordnet')
titulos = titulos_noticias()

# Definir el set de palabras a omitir
stop_words = set(stopwords.words('spanish'))
# Considerar omitir signos de puntuacion comunes
stop_words.update([',', ':', '?', 'así', '``', '.', '\'\''])

# La lematizacion busca la raiz de la palabra
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Preprocesa un texto realizando tokenización, conversión a minúsculas,
    lematización y eliminación de palabras vacías (stop words).

    Este método toma un texto de entrada y realiza los siguientes pasos:
    1. Convierte todo el texto a minúsculas.
    2. Tokeniza el texto en palabras.
    3. Elimina las palabras vacías (stop words).
    4. Lematiza cada palabra restante para reducirla a su forma base.

    Parámetros:
    -----------
    text : str
        El texto de entrada que se desea preprocesar.

    Retorna:
    --------
    tokens : list
        Una lista de tokens procesados y lematizados,
        con las palabras vacías eliminadas.

    Ejemplo:
    --------
    >>> text = "Este es un ejemplo de texto para preprocesar."
    >>> tokens = preprocess_text(text)
    >>> print(tokens)
    ['ejemplo', 'texto', 'preprocesar']
    """
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens


# Preprocesar los titulos
processed_titles = [preprocess_text(text) for text in titulos]

# Crear un diccionario un corpus
dictionary = corpora.Dictionary(processed_titles)

# Convertir los documentos a formato bag-of-words
corpus = [dictionary.doc2bow(text) for text in processed_titles]

# Crear el modelo LDA
lda_model = models.LdaModel(corpus, num_topics=3, 
                            id2word=dictionary, passes=15)

# Obtener los temas
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)

all_titles = list(chain.from_iterable(processed_titles))
# Crear la word cloud
wordcloud = WordCloud(width=800, height=400, 
                      background_color='white').generate(' '.join(all_titles))

# Mostrar la word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# Guardar la imagen
plt.savefig("nube_temas_principales.png")
plt.show()

