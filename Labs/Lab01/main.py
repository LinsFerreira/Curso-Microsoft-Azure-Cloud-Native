import streamlit as st
from azure.storage.blob import BlobServiceClient
import pyodbc
import uuid
import json
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Importa variáveis do Azure Storage
BlobConnectionString = os.getenv('CONNECTION_STRING')
BlobContainerName = os.getenv('CONTAINER_NAME')
BlobAccountName = os.getenv('ACCOUNT_NAME')

# Importa as variáveis de conexão com BD SQL
SQL_SERVER   = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USERNAME = os.getenv('SQL_USERNAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

# String de conexão ODBC
ODBC_STRING = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USERNAME};PWD={SQL_PASSWORD}"

# Verifica a conexão com tratamento de erro
try:
    conn = pyodbc.connect(ODBC_STRING)
    cursor = conn.cursor()

    # Exemplo de uso: testar se a conexão funciona
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("Conexão bem-sucedida. Resultado:", result[0])

except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)

# Título da aplicação
st.title("Cadastro de Produto - E-Commerce na Cloud")

# Formulário para cadastro do produto
product_name = st.text_input("Nome do Produto")
description = st.text_area("Descrição do Produto")
price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
uploaded_file = st.file_uploader("Imagem do Produto", type=["png", "jpg", "jpeg"])

# Função para enviar imagem para o Azure Blob Storage
def upload_image(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BlobConnectionString)
        container_client = blob_service_client.get_container_client(BlobContainerName)
        blob_name = f"{uuid.uuid4()}.jpg"
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file.read(), overwrite=True)
        image_url = f"https://{BlobAccountName}.blob.core.windows.net/{BlobContainerName}/{blob_name}"
        return image_url
    except Exception as e:
        st.error(f"Erro ao enviar imagem: {e}")
        return None

# Função para inserir os dados do produto no Azure SQL Server usando pyodbc
def insert_product_sql(product_data):
    try:
        conn = pyodbc.connect(ODBC_STRING)
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO dbo.Produtos (nome, descricao, preco, imagem_url)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            product_data["nome"],
            product_data["descricao"],
            product_data["preco"],
            product_data["imagem_url"]
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir no Azure SQL: {e}")
        return False

# Função para listar os produtos do Azure SQL Server
def list_products_sql():
    try:
        conn = pyodbc.connect(ODBC_STRING)
        cursor = conn.cursor()
        query = "SELECT id, nome, descricao, preco, imagem_url FROM dbo.Produtos"
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        cursor.close()
        conn.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []

# Função para exibir a lista de produtos na tela   
def list_produtos_screen():
    products = list_products_sql()
    if products:
        cards_por_linha = 3
        cols = st.columns(cards_por_linha)
        for i, product in enumerate(products):
            col = cols[i % cards_por_linha]
            with col:
                st.markdown(f"### {product['nome']}")
                st.write(f"**Descrição:** {product['descricao']}")
                st.write(f"**Preço:** R$ {product['preco']:.2f}")
                if product["imagem_url"]:
                    html_img = f'<img src="{product["imagem_url"]}" width="200" height="200" alt="Imagem do produto">'
                    st.markdown(html_img, unsafe_allow_html=True)
                st.markdown("---")
            if (i + 1) % cards_por_linha == 0 and (i + 1) < len(products):
                cols = st.columns(cards_por_linha)
    else:
        st.info("Nenhum produto encontrado.")

# Botão para cadastro do produto
if st.button("Cadastrar Produto"):
    if not product_name or not description or price is None:
        st.warning("Preencha todos os campos obrigatórios!")
    else:
        image_url = ""
        if uploaded_file is not None:
            image_url = upload_image(uploaded_file)
        
        product_data = {
            "nome": product_name,
            "descricao": description,
            "preco": price,
            "imagem_url": image_url
        }

        if insert_product_sql(product_data):
            st.success("Produto cadastrado com sucesso no Azure SQL!")
            list_produtos_screen()
        else:
            st.error("Houve um problema ao cadastrar o produto no Azure SQL.")

        file_path = "produtos.json"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    produtos = json.load(f)
                except json.JSONDecodeError:
                    produtos = []
        else:
            produtos = []

        produtos.append(product_data)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)
        
        st.json(product_data)

st.header("Listagem dos Produtos")

# Botão para carregar e exibir a lista de produtos
if st.button("Listar Produtos"):
    list_produtos_screen()
