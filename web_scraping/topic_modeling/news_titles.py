import requests # type:ignore
from bs4 import BeautifulSoup # type:ignore


def get_response(url:str, tag:str, tag_class:str):
    """ Hacer request http a una url y traer su respuesta html, filtrada por:
    un tag html con un atributo class en especifico.

    Args:
    url: Direccion url de la pagina web
    tag: Tipo de tag a buscar
    tag_class: Atributo class de los tag a buscar

    Returns:
    Lista de objetos BeautifulSoup, segun la busqueda aplicada
    """
    # Realiza la solicitud HTTP a la página
    response = requests.get(url)
    # Verifica si la solicitud fue exitosa
    response.raise_for_status()

    # Contenido de la página a html
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra todos los tag con class=""
    elements = soup.find_all(tag, class_=tag_class)
    return elements


# Para analizar los temas de los titulares,
# debemos eliminar palabras que no aportan al titular y que
# unicamente sirven como identificadores de la noticia.
def limpiar_string(cadena:str):
    """Limpia una cadena dividiéndola por '|' y devolviendo la parte posterior.

    Args:
    cadena: La cadena a limpiar.

    Returns:
    La cadena sin la parte anterior a '|'.
    """

    partes = cadena.split('|')
    # Si del split() devuelve mas de un elemento,
    # quiere decir que ese string contenia '|'
    if len(partes) > 1:
    # En ese caso devolvemos unicamente la parte posterior al '|'
    # que seria unicamente el titular y sin etiquetas
        return partes[1].strip()
    # Independienmente del caso, eliminamos posibles tabulaciones o espacios
    # innecesarios con .strip()
    else:
        return cadena.strip()
    

def titulos_noticias():
    """Funcion auxiliar para consultar noticias de diversos sitios
    """
    # URL de CNN en español
    url_cnn = 'https://cnnespanol.cnn.com/'
    # Encuentra todos los <h2> con class="news__title"
    h2_elements = get_response(url=url_cnn, tag='h2', tag_class='news__title')

    # Extrae el texto de los <a> dentro de los <h2>
    titles_cnn = [str(h2.find('a').get_text()) for h2 in h2_elements if h2.find('a')]
    titles_cnn = [limpiar_string(t) for t in titles_cnn]
    # print(titles_cnn)

    # URL de la BBC
    url_bbc = 'https://www.bbc.com/mundo'
    div_elements = get_response(url=url_bbc, tag='div', tag_class='promo-text')
    titles_bbc = [str(div.find('h3').find('a').get_text()) for div in div_elements if div.find('h3').find('a')]
    titles_bbc = [limpiar_string(t) for t in titles_bbc]

    # Los ultimos titulos de la BBC que coinciden con la busqueda,
    # son sus redes sociales
    titles_bbc = titles_bbc[:-7]
    # print(titles_bbc)

    return titles_cnn + titles_bbc
