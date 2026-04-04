# 💰 Controle Financeiro CLI em Python

Aplicação simples de **controle financeiro pessoal em Python** que permite importar extratos bancários em CSV, registrar transações manualmente e gerar relatórios de despesas utilizando um banco de dados local.

O sistema roda em **linha de comando (CLI)** e utiliza **SQLite** como banco de dados local.

---

# 📌 Funcionalidades

* Importar extrato bancário em CSV
* Registrar transações manualmente
* Remover transações
* Visualizar saldo atual
* Relatório de despesas mensais
* Armazenamento local em banco SQLite
* Estrutura simples e fácil de evoluir

---

# 🧱 Estrutura do Projeto

```
financas_app/
│
├── app.py
├── database.py
├── financas.py
├── importador_csv.py
├── README.md
├── Dockerfile
├── .dockerignore
└── financas.db (criado automaticamente)
```

Descrição dos arquivos:

| Arquivo           | Descrição                                      |
| ----------------- | ---------------------------------------------- |
| app.py            | Ponto de entrada da aplicação e menu principal |
| database.py       | Conexão e criação das tabelas do banco         |
| financas.py       | Funções de manipulação das transações          |
| importador_csv.py | Importação de extratos CSV                     |
| financas.db       | Banco SQLite gerado automaticamente            |

---

# 🗄 Estrutura do Banco de Dados

## Tabela `transacoes`

Armazena todas as movimentações financeiras.

| Campo     | Tipo    | Descrição                  |
| --------- | ------- | -------------------------- |
| id        | INTEGER | Identificador da transação |
| data      | TEXT    | Data da transação          |
| descricao | TEXT    | Descrição                  |
| tipo      | TEXT    | credito ou debito          |
| valor     | REAL    | Valor da transação         |
| origem    | TEXT    | origem (manual ou csv)     |

---

## Tabela `salario`

Armazena configuração do salário mensal.

| Campo         | Tipo    |
| ------------- | ------- |
| id            | INTEGER |
| valor         | REAL    |
| dia_pagamento | INTEGER |

---

## Tabela `salario_lancado`

Controla os meses em que o salário já foi creditado.

| Campo | Tipo    |
| ----- | ------- |
| id    | INTEGER |
| mes   | INTEGER |
| ano   | INTEGER |

---

# 📥 Formato do Arquivo CSV

O arquivo CSV deve possuir as seguintes colunas:

```
data,descricao,valor
2026-01-01,Salario,5000
2026-01-03,Supermercado,-150
2026-01-05,Internet,-100
```

Regras:

* valores **positivos** são considerados **crédito**
* valores **negativos** são considerados **débito**

---

# ⚙️ Requisitos

* Python 3.9 ou superior

Download do Python:
https://www.python.org/downloads/

O sistema utiliza apenas bibliotecas padrão do Python:

* csv
* sqlite3

Nenhuma dependência externa é necessária.

---

# 🚀 Executando a Aplicação

## 1️⃣ Entrar na pasta do projeto

```
cd financas_app
```

---

## 2️⃣ Executar o aplicativo

```
python app.py
```

ou

```
python3 app.py
```

---

## 3️⃣ Menu principal

Ao iniciar o sistema será exibido:

```
=== CONTROLE FINANCEIRO ===

1 - Importar extrato CSV
2 - Adicionar transação
3 - Deletar transação
4 - Mostrar saldo
5 - Relatório despesas
0 - Sair
```

---

# 📊 Exemplos de Uso

### Adicionar transação manual

```
Data: 2026-03-12
Descrição: Mercado
Tipo (credito/debito): debito
Valor: 150
```

---

### Mostrar saldo

```
Saldo atual: R$ 2350.00
```

---

### Relatório de despesas

```
Despesas por mês

2026-01  R$ 1200
2026-02  R$ 980
2026-03  R$ 650
```

---

# 🐳 Executando com Docker

Também é possível executar o projeto utilizando **Docker**, sem precisar instalar Python no computador.

---

## 1️⃣ Build da imagem Docker

Na pasta do projeto execute:

```
docker build -t financas-python .
```

Isso criará uma imagem chamada:

```
financas-python
```

---

## 2️⃣ Executar o container

```
docker run -it financas-python
```

O menu da aplicação será exibido no terminal.

---

## 3️⃣ Executar com persistência do banco de dados

Para garantir que o banco SQLite seja salvo no computador (host):

### Linux / Mac

```
docker run -it -v $(pwd):/app financas-python
```

### Windows PowerShell

```
docker run -it -v ${PWD}:/app financas-python
```

Assim o arquivo do banco será salvo localmente:

```
financas.db
```

---

# 📦 Estrutura Docker

Arquivos utilizados para execução em container:

```
Dockerfile
.dockerignore
```

---

# 🧠 Possíveis Melhorias Futuras

* Sistema de categorias de despesas
* Lançamento automático de salário
* Contas recorrentes
* Exportação para Excel
* Dashboard com gráficos
* Interface gráfica
* API REST

Para evoluir o projeto pode-se utilizar:

* **SQLAlchemy** para modelagem do banco
* **FastAPI** para criar uma API
* **React** para interface web

---

# 📜 Licença

Projeto livre para uso pessoal e educacional.

---

# 👨‍💻 Autor

Projeto criado para estudos e automação financeira pessoal utilizando Python.
