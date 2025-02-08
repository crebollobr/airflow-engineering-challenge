# Teste de Airflow

Este projeto consiste na criação de uma configuração do Airflow em um ambiente Docker, incluindo a criação de DAGs para orquestração de tarefas. Para mais detalhes, consulte o repositório oficial: [airflow-engineering-challenge](https://github.com/claudioviniciuso/airflow-engineering-challenge).

---

## Alterações no `docker-compose.yaml`

Foram realizadas várias melhorias no arquivo `docker-compose.yaml` para aumentar a segurança, monitoramento e estabilidade do ambiente Airflow. Abaixo estão as principais alterações:

1. **Definição da Fernet Key**  
   - **Antes:** Vazia.  
   - **Agora:** `'JsDQTWP3D93rCe71-8_4ojiRK09gF6EcioGQBhKqOuk='`.  
   - **Impacto:** Melhora a segurança ao criptografar conexões e senhas armazenadas no Airflow.

2. **Adição do serviço `airflow-flower`**  
   - **Descrição:** Adicionei o serviço para monitorar o Celery através do **Airflow Flower**.  
   - **Porta:** Exponho a interface na porta `5555:5555`.

3. **Correção da porta do healthcheck do scheduler**  
   - **Antes:** Porta `8974`.  
   - **Agora:** Porta `8793`.  
   - **Impacto:** Garante que o teste de saúde funcione corretamente.

4. **Modificação da variável `DUMB_INIT_SETSID`**  
   - **Antes:** `"0"`.  
   - **Agora:** `"1"`.  
   - **Impacto:** Melhora a compatibilidade e estabilidade dos processos.

5. **Ajustes de permissões e diretórios**  
   - **Descrição:** Criei o diretório `/sources/logs/scheduler` para organizar melhor os logs.  
   - **Impacto:** Ajustei as permissões para garantir acesso adequado aos diretórios de logs, DAGs e plugins.

Para mais detalhes, consulte o commit: [1549db3](https://github.com/crebollobr/airflow-engineering-challenge/commit/1549db315402739ff4d3f6d25102a3219319fc42).

---

## Definição de Variáveis do Airflow

### Conexão API
- **Nome:** `api_auth`  
- **Credenciais:** `admin/admin`  
- **URL:** `http://api:800/token`

### Variável gloval
- **api_token_url:** `http://api:8000/token`
### Variável de acordo com o tipo de dado  
- **api_products_url:** `http://api:8000/api/v1/products`
- **api_token_products_local_storage:** `local_storage/raw/products/{date_path}/`  
- **api_products_file:** `products_{timestamp}.json`

- **api_carts_url:** `http://api:8000/api/v1/carts`  
- **api_token_carts_local_storage:** `local_storage/raw/carts/{date_path}/`  
- **api_carts_file:** `carts_{timestamp}.json`

- **api_customer_url:** `http://api:8000/api/v1/customer`  
- **api_token_customer_local_storage:** `local_storage/raw/customer/{date_path}/`  
- **api_customer_file:** `customer_{timestamp}.json`

- **api_logistict_url:** `http://api:8000/api/v1/logistict`  
- **api_token_logistict_local_storage:** `local_storage/raw/logistict/{date_path}/`  
- **api_logistict_file:** `logistict_{timestamp}.json`

---

## Criação das DAGs

Foram criadas as seguintes DAGs:
- **customer.py**  
- **logistict.py**  
- **products.py**

Para visualizar os arquivos, acesse o diretório de DAGs no repositório: [DAGs](https://github.com/crebollobr/airflow-engineering-challenge/tree/main/DAGS).

---

### Melhorias Gerais
- **Segurança:** Configuração da Fernet Key para criptografia.  
- **Monitoramento:** Adição do serviço Flower para monitoramento do Celery.  
- **Organização:** Ajustes de permissões e criação de diretórios para logs.  
- **Estabilidade:** Correção de portas e variáveis para melhor funcionamento.

Este ambiente está pronto para ser utilizado em um cenário de produção, com melhorias significativas em relação à configuração inicial.
