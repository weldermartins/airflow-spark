###  O contexto do projeto será normalizar os arquivos json que estão dentro da pasta Datalake, utilizando o Airflow como orquestrador e o Spark para ingestão.

### Execute o comando para criar a imagem e container 
```bash
docker-compose up -d --build 
```

### Execute o comando para subir o container
```bash
docker-compose up -d 
```

### O arquivo Dockerfile irá baixar e setar as variaveis:</br>
* Java
* python
* spark</br>
![scheme](images/variaveis.png)</br>
    

### Criando a conexão Spark no Airflow </br>
![scheme](images/conexao-spark2.png)</br>

### A primeira DAG irá fazer uma contagem de cada palavra de um texto </br>
![scheme](images/primeiradag.png)</br>

### A primeira DAG irá fazer uma contagem de cada palavra de um texto </br>
![scheme](images/primeiradag.png) </br>

### Retorno da DAG </br>
![scheme](images/dag1.png) </br>


### Segunda Dag traz um exemplo de normalização de dados </br>
![scheme](images/segundadag.png) </br>

