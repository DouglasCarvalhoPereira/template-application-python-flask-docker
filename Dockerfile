# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os requisitos do projeto para o container
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o container
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]