# Use uma imagem Python oficial como base
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR src/

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para executar a aplicação quando o contêiner for iniciado
CMD ["python", "main.py"]
