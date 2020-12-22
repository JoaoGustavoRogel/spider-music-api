# Spider Music

<p align="center">
  <img src="docs/images/logo.png" width="300px"/>
</p>

![Python](https://img.shields.io/badge/Python-%3E%3D%203.7-blue)
![MIT](https://img.shields.io/badge/license-MIT-green)
![Continuous Integration](https://github.com/JoaoGustavoRogel/api-data-c214/workflows/Continuous%20Integration/badge.svg)

## Descrição

O projeto **Spider Music** foi desenvolvido como projeto final para a disciplina de *Engenharia de Software (C214)* no *Instituto Nacional de Telecomunicações (INATEL)*, aplicando os conceitos aprendidos na disciplina, como o uso de gerenciadores de dependências, padrões de projeto, testes de classes e testes mock, bem como outros conceitos abordados em outras disciplinas, como POO e integração com bancos de dados.

O **Spider Music** consiste de uma api que permite a consulta de dados do serviço de streaming *[Spotify](https://www.spotify.com/br/)*, e retorna dados de charts e informações detalhadas sobre músicas, álbuns e artistas. O uso da api se dá através de um endpoint, que permite a realização de consultas e a interação com o banco de dados, permitindo inserções, consultas, updates e remoções.

Os dados coletados podem então ser utilizados em outros projetos, como dashboards apresentando os charts e algoritmos capazes de realizar previsões de como um determinado lançamento pode se comportar no futuro.

## Escopo

O **Spider Music** pode ser separado em três área principais: a coleta dos dados, a interface de comunicação com o banco de dados e os endpoints de acesso.

A coleta dos dados se dá por meio de dois crawlers, um deles responsável pelos dados de charts e outro responsável pela interação com a api própria do Spotify. Ambos os crawlers recebem parâmetros para realizarem a coleta, e a partir deles, consegue selecionar de forma correta as informações que são de fato relevantes e importantes para o usuário. 

A segunda área é a responsável por servir como interface de comunicação com o banco de dados. Ela é responsável por gerenciar as inserções, buscas, alterações e remoções de dados de forma automática, bastando apenas que o usuário faça a chamada do endpoint responsável pela ação desejada. 

Por fim, os endpoints são responsáveis por facilitar o uso da api, permitindo que o usuário não precise executar o projeto em sua máquina para realizar as consultas. Os endpoints foram desenvolvidos com a tecnologia REST, e permitem o uso das funcionalidades a partir de requisições de URLs específicas para cada tipo de ação. Essas requisições exigem parâmetros que indicam detalhes que serão utilizados na função desejada, como por exemplo, qual deve ser a música ou artista buscado ou qual é o período e localidade dos charts desejados.

## Funcionalidades

O usuário pode realizar as quatro operações básicas dos bancos de dados (inserção, busca, atualização e remoção) com os dados coletados pela api. Esses dados podem ser dos charts regionais ou dados específicos de músicas, álbuns e artistas.

Estão disponíveis as seguintes funções:

* Busca de dados diretamente do crawler;
* Inserção dos dados coletados no banco de dados;
* Busca dos dados presentes no banco de dados;
* Update dos dados presentes no banco de dados;
* Remoção dos dados presentes no banco de dados.

## Bibliotecas

As bibliotecas utilizadas no projeto foram:

* [fastapi](https://pypi.org/project/fastapi/)
* [mock](https://pypi.org/project/mock/)
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
* [numpy](https://pypi.org/project/numpy/)
* [pandas](https://pypi.org/project/pandas/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [requests](https://pypi.org/project/requests/)
* [spotipy](https://pypi.org/project/spotipy/)

## Ferramentas

* [Python (Anaconda)](https://www.anaconda.com/products/individual)
* [Pytest](https://docs.pytest.org/en/stable/)
* [Unittest](https://docs.python.org/3/library/unittest.html)
* [Mock](https://docs.python.org/3/library/unittest.mock.html)
* [MySQL](https://www.mysql.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

## Como Usar

O projeto possui os seguintes requisitos:

* Python >= 3.7 (Distribuição Recomendada: Anaconda)
* MySQL Server
* Bibliotecas encontradas no requirements.txt

Para executar a api:

```
  uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
Não esquecer de entrar dentro da pasta `api`.

Após executar o comando acima, a api está pronta para o uso. Os seguintes endpoints estão disponíveis:

```
  0.0.0.0:8000/spotify/chart/crawler_query
  0.0.0.0:8000/spotify/chart/insert_db
  0.0.0.0:8000/spotify/chart/query_db
  0.0.0.0:8000/spotify/chart/delete_db
  0.0.0.0:8000/spotify/chart/update_db
  0.0.0.0:8000/spotify/api/crawler_track
  0.0.0.0:8000/spotify/api/insert_track
  0.0.0.0:8000/spotify/api/delete_track
  0.0.0.0:8000/spotify/api/update_track
  0.0.0.0:8000/spotify/api/crawler_album
  0.0.0.0:8000/spotify/api/insert_album
  0.0.0.0:8000/spotify/api/delete_album
  0.0.0.0:8000/spotify/api/update_album
  0.0.0.0:8000/spotify/api/crawler_artist
  0.0.0.0:8000/spotify/api/insert_artist
  0.0.0.0:8000/spotify/api/delete_artist
  0.0.0.0:8000/spotify/api/update_artist
```

Para utilizar os endpoins, é necessário fornecer alguns parâmetros. Os endpoints que coletam dados de charts precisam de dois parâmetros: `start_date` e `end_date` (a data de início e a data do fim da pesquisa, respectivamente), que são passadas no formato `YYYY-MM-DD`. Já os endpoints que coletam os dados diretamente do Spotify requerem apenas um parâmetro, o `id`, que é uma string contendo o identificador único que indica qual é a música, álbum ou artista.

Seguem abaixo dois exemplos de uso:

```
  0.0.0.0:8000/spotify/chart/crawler_query?start_date=2020-12-01&end_date=2020-12-10

  0.0.0.0:8000/spotify/api/crawler_track?id=1ayaOin9hxCtyhg4UsBTpg
```

A resposta da requisição em ambos os casos é um json, contendo o campo `data`, que possui os dados desejados.

