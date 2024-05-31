# API Golden Raspberry Awards

Esta API RESTful permite a leitura da lista de indicados e vencedores da categoria Pior Filme do Golden Raspberry Awards.

## Requisitos

- Python 3.6+
- Pip

## Instalação

1. Clone o repositório:
    ```sh
    git clone <url_do_repositorio>
    cd <nome_do_repositorio>
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Executando a Aplicação

1. Inicie a aplicação:
    ```sh
    python app.py
    ```

2. Acesse a API em `http://127.0.0.1:5000/producers/intervals`.

## Executando os Testes de Integração

1. Execute os testes:
    ```sh
    python -m unittest discover
    ```

## Estrutura do Projeto

- `app.py`: Define a API e seus endpoints.
- `models.py`: Define o modelo de dados e a configuração do banco de dados.
- `utils.py`: Contém funções auxiliares para manipulação de dados.
- `test_integration.py`: Testes de integração.
- `movies.csv`: Arquivo CSV contendo os dados.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Instruções para rodar o projeto e os testes de integração.
