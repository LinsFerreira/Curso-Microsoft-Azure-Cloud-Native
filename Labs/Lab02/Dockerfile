FROM nginx:alpine

# Copia os arquivos do site para o container
COPY ./html /usr/share/nginx/html

# Expôe a porta 8080
EXPOSE 8080

# Comando para executar o nginx em background

CMD ["nginx", "-g", "daemon off;"]
