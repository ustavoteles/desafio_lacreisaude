# Use uma imagem base do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Verifique os arquivos no diretório /app
RUN ls -l /app

# Instala as dependências do projeto
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copia o restante do código do projeto
COPY . .

# Expõe a porta que o Django vai rodar
EXPOSE 8000

# Comando para rodar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
