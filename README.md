# Spider Music

![Continuous Integration](https://github.com/JoaoGustavoRogel/api-data-c214/workflows/Continuous%20Integration/badge.svg)

## Descrição

O projeto **Spider Music** foi desenvolvido como projeto final para a disciplina de *Engenharia de Software (C214)* no *Instituto Nacional de Telecomunicações (INATEL)*, aplicando os conceitos aprendidos na disciplina, como o uso de gerenciadores de dependências, padrões de projeto, testes de classes e testes mock, bem como outros conceitos abordados em outras disciplinas, como POO e integração com bancos de dados.

Foram utilizadas as seguintes ferramentas:

* [Python (Anaconda)](https://www.anaconda.com/products/individual)
* [MySQL](https://www.mysql.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

O projeto **Spider Music** é uma api que permite a consulta de dados do serviço de streaming *[Spotify](https://www.spotify.com/br/)*, e retorna dados de charts e informações detalhadas sobre músicas, álbuns e artistas. O uso da api se dá através de um endpoint, que permite a realização de consultas e a interação com o banco de dados, permitindo inserções, consultas, updates e remoções.

Os dados coletados podem então ser utilizados em outros projetos, como dashboards apresentando os charts e algoritmos capazes de realizar previsões de como um determinado lançamento pode se comportar no futuro.

## Escopo

O **Spider Music** pode ser separado em três área principais: a coleta dos dados, a interface de comunicação com o banco de dados e os endpoints de acesso.

A coleta dos dados se dá por meio de dois crawlers, um deles responsável pelos dados de charts e outro responsável pela interação com a api própria do Spotify. Ambos os crawlers recebem parâmetros para realizarem a coleta, e a partir deles, consegue selecionar de forma correta as informações que são de fato relevantes e importantes para o usuário. 

A segunda área é a responsável por servir como interface de comunicação com o banco de dados. Ela é responsável por gerenciar as inserções, buscas, alterações e remoções de dados de forma automática, bastando apenas que o usuário faça a chamada do endpoint responsável pela ação desejada. 

Por fim, os endpoints são responsáveis por facilitar o uso da api, possibilitando que o usuário não precise executar o projeto em sua máquina para realizar as consultas. Os endpoints foram desenvolvidos com a tecnologia REST, e permitem o uso das funcionalidades a partir de requisições de urls específicas para cada tipo de ação. Essas requisições exigem parâmetros que indicam o que detalhes a serem usados na função desejada, como por exemplo, indicando qual deve ser a faixa buscada ou qual é o período e localidade dos charts desejados.

## Funcionalidades

O usuário pode realizar as quatro operações básicas dos bancos de dados (inserção, busca, atualização e remoção) com os dados coletados pela api. Esses dados podem ser dos charts regionais ou dados específicos de músicas, álbuns e artistas.

Estão disponíveis as seguintes funções:

* Busca de dados diretamente do crawler;
* Inserção dos dados coletados no banco de dados;
* Busca dos dados presentes no banco de dados;
* Update dos dados presentes no banco de dados;
* Apagar dados presentes no banco de dados.

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

## Como Usar

O projeto possui os seguintes requisitos

* Python >= 3.7 (Distribuição Recomendada: Anaconda)
* MySQL Server
* Bibliotecas encontradas no requirements.txt

Para executar a api:

```
  uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
Não esquecer de entrar dentro da pasta `api`.
