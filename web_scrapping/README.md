## *expired_domains.py*
Busca dominios expirados dentro de [www.expireddomains.net](https://www.expireddomains.net), usando selenium.
En este ejemplo el navegador usado es Chrome driver.

## *topic_modeling*
  ### 'news_titles.py'
  Utiliza beautifulsoup4 y requests, para buscar los titulares de la pantalla de inicio de los noticieros: BBC y CNN; en español.

  ### 'temas_principales.py'
  Con nltk y gensim se hace un topic modeling de los titulares extraidos a traves de un modelo LDA, ademas se haec una nube de palabras de las palabras mas comunes de los titulares.

  Este ejemplo se corrio el 22 de agosto del 2024:

  ![](web_scrapping/topic_modeling/nube_temas_principales.png)
