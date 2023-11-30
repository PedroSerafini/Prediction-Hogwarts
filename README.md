#Projeto API de Sugestão de Valores para Imóveis de Hogwarts

Este projeto implementa uma API que fornece sugestões de valores de aluguel e venda para imóveis próximos à Escola de Magia de Hogwarts. A API é desenvolvida em Python usando o framework Flask e utiliza um modelo de Machine Learning para realizar as previsões.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- app.py: O arquivo principal que contém a implementação da API Flask e o código para treinar e usar o modelo de Machine Learning.

- hogwarts_dataset.csv: O conjunto de dados em formato CSV contendo informações sobre os imóveis utilizadas para treinar o modelo.

- templates/: Esta pasta é destinada a armazenar arquivos de template se você estiver usando Flask para renderizar páginas web.

- README.md: Este arquivo que fornece informações sobre o projeto.

## Configuração e Execução

Instale as dependências necessárias executando o seguinte comando no terminal:

'''bash
pip install pandas scikit-learn Flask
'''

Execute a aplicação Flask com o seguinte comando:

'''bash
flask run
'''

Certifique-se de que o arquivo app.py está no diretório atual e que o Flask está instalado corretamente.

Acesse a aplicação no navegador em http://127.0.0.1:5000/ ou utilize ferramentas como o Postman para fazer solicitações à API.

## Uso da API

A API possui uma rota /sugerir_valores que aceita solicitações POST contendo informações sobre um imóvel. Os parâmetros esperados incluem:

Número de Quartos
Número de Banheiros
Número de Garagens (para Vassouras Mágicas)
Metros Quadrados
Número de Encantamento
Se possui quadra para Quadribol

Exemplo de solicitação:

Execute a aplicaçâo Flask e preencha os campos do HTML, e entâo clique em "Enviar".
A API retornará sugestões de valores de aluguel e venda para o imóvel com base no modelo treinado.

## Observações

Certifique-se de que o ambiente Python está configurado corretamente e que todas as dependências estão instaladas antes de executar o projeto. Este README.md fornece uma visão geral do projeto e das etapas para executá-lo, mas ajustes adicionais podem ser necessários dependendo das configurações específicas do seu ambiente.





