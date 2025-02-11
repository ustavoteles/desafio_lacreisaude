# Desafio LacreiSaude

Este projeto foi realizado como parte de um desafio voluntário para a vaga de Backend Developer na Lacrei Saúde, com o objetivo de aprimorar as habilidades de desenvolvimento em Django, APIs RESTful e Banco de Dados Relacional.
Este projeto é uma API para o gerenciamento de consultas e profissionais de saúde, desenvolvida com Django, Django REST Framework e PostgreSQL. A aplicação foi projetada para facilitar a gestão de dados de profissionais da saúde e suas consultas, permitindo operações como criação, leitura, atualização e exclusão dessas entidades.
A API foi configurada para rodar em contêineres Docker, o que garante um ambiente de desenvolvimento consistente e fácil de configurar em diferentes máquinas. Além disso, a documentação da API foi gerada automaticamente utilizando o Swagger.

## Descrição

Este repositório contém a API de um sistema de saúde para gerenciamento de profissionais e consultas. A API oferece funcionalidades de CRUD (Criar, Ler, Atualizar e Deletar) para ambos os recursos.

- **Profissionais**: Cadastro de profissionais de saúde com dados como nome, especialização e contato.
- **Consultas**: Registro de consultas realizadas, associando-as aos profissionais de saúde.

## Pré-Requisitos

Antes de começar, você precisará ter instalado em sua máquina:

- Docker e Docker Compose
- Python 3.12 ou superior
- Poetry


## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido e escalável.
- **Django REST Framework**: Para construção da API.
- **Psycopg2-binary**: Conector para o banco de dados PostgreSQL.
- **Pytest**: Framework para testes.
- **Pytest-django**: Plugin do Pytest para integração com Django.
- **Drf-yasg**: Para gerar documentação da API com Swagger.
- **PostgreSQL**: Banco de dados relacional utilizado.
- **Docker e Docker Compose**: Para gerenciar o ambiente de desenvolvimento.

## Instruções de Instalação

1. Certifique-se de ter o Python e Docker instalados em sua máquina.
2. Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```

3. Navegue até o diretório do projeto:
    ```bash
    cd desafio_lacreisaude
    ```

4. Instale as dependências com o Poetry:
    ```bash
    poetry install
    ```

5. Compile e suba os containers Docker:
    ```bash
    docker-compose up --build
    ```

6. Execute as migrações do banco de dados:
    ```bash
    poetry run python manage.py migrate
    ```

7. Para acessar o aplicativo, vá para [http://localhost:8000/swagger](http://localhost:8000/swagger).

# Estrutura do Projeto
A estrutura do projeto segue a seguinte organização:
```
desafio_lacreisaude/
├── desafio_lacreisaude/        # Configuração principal do Django
│   ├── settings.py             # Configurações do projeto
│   ├── urls.py                 # Configurações de URLs
│   └── wsgi.py                 # Configurações para o servidor WSGI
├── consulta/                   # Modelo e views relacionadas a consultas
│   ├── models.py               # Modelos de dados para consultas
│   ├── serializers.py          # Serializers para consultas
│   └── views.py                # Views para consulta
├── profissional/               # Modelo e views relacionadas aos profissionais
│   ├── models.py               # Modelos de dados para profissionais
│   ├── serializers.py          # Serializers para profissionais
│   └── views.py                # Views para profissionais
├── manage.py                   # Script para rodar os comandos do Django
├── Dockerfile                  # Dockerfile para o ambiente de produção
├── docker-compose.yml          # Docker Compose para orquestrar containers
└── pyproject.toml              # Arquivo de configuração do Poetry
```

# Documentação da API
A documentação da API é gerada automaticamente utilizando o Drf-yasg. Você pode acessá-la no seguinte endpoint após rodar o servidor:
```bash
http://localhost:8000/swagger/
```
A documentação será exibida em formato Swagger, onde você pode ver todas as rotas, detalhes dos endpoints e até mesmo testar as funcionalidades da API diretamente pela interface web.

# Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
Copyright (c) 2025 Gustavo Teles