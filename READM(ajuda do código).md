📘 Anotação Técnica do Seu Código (keywords + funções embutidas)

Vou usar exemplos do seu próprio projeto.


---

🔹 import

Palavra-chave usada para importar arquivos ou módulos.

import os
import json

O que faz:

Permite usar bibliotecas prontas do Python.

No seu código:

os → mexe com arquivos e pastas

json → salva e lê dados em formato JSON



---

🔹 from ... import ...

Importa partes específicas de outro arquivo.

from perfil import perfil_existe, criar_perfil

Vantagem:

Importa só o necessário.


---

🔹 def

Define uma função.

def criar_perfil():

Estrutura:

def nome_da_funcao():

No seu código:

Você criou várias funções:

criar_perfil()

listar_perfis()

escolher_perfil()

menu()



---

🔹 return

Retorna um valor e encerra a função.

return carregar_perfil(nome)

Significa:

A função entrega um resultado.

Exemplo:

escolher_perfil() devolve um perfil carregado.


---

🔹 while

Loop de repetição enquanto a condição for verdadeira.

while True:

Significa:

Repete infinitamente até encontrar break ou return.


---

🔹 True

Valor booleano verdadeiro.

while True:

Equivale a:

"enquanto for verdadeiro"


---

🔹 if

Condição.

if len(nome) < 3:

Lê-se:

Se tamanho do nome for menor que 3.


---

🔹 elif

Outra condição intermediária.

elif op == "2":

Significa:

Se o if anterior não acontecer, testa isso.


---

🔹 else

Caso nenhuma condição anterior aconteça.

else:
    print("Opção inválida.")


---

🔹 break

Interrompe o loop.

break

No seu código:

Sai do while quando o dado está correto.


---

🔹 continue

Pula para a próxima repetição.

continue

Exemplo:

Se nome inválido:

if len(nome) < 3:
    continue

Volta para pedir de novo.


---

🔹 input()

Recebe entrada do usuário.

nome = input("Nome do perfil: ")

Sempre retorna:

Texto (str)


---

🔹 .strip()

Método de string.

nome.strip()

Remove:

Espaços no começo e fim.

Exemplo:

" Felipe ".strip()

vira:

"Felipe"


---

🔹 .lower()

Transforma em minúsculas.

resposta.lower()

Exemplo:

"SIM".lower()

vira:

"sim"


---

🔹 len()

Conta tamanho.

len(nome)

Exemplo:

len("Felipe")

resultado:

6


---

🔹 print()

Mostra texto no terminal.

print("Olá")


---

🔹 f-string

Interpolação de variáveis.

print(f"Olá {perfil['nome']}")

O f permite colocar variável dentro da string.


---

🔹 [] (colchetes)

Usado para acessar dicionário ou lista.

perfil["nome"]

Aqui:

Acessa valor da chave "nome".


---

🔹 Dicionário {}

Estrutura chave → valor.

{"nome": nome}

No seu projeto:

{
 "nome": "Felipe",
 "conhecimento_financeiro": "sim"
}


---

🔹 in

Verifica existência.

if "conhecimento_financeiro" in perfil:

Lê-se:

Se essa chave existir no dicionário.


---

🔹 not

Negação lógica.

if not perfil_existe():

Lê-se:

Se NÃO existir perfil.


---

🔹 and

Duas condições ao mesmo tempo.

os.path.exists(CAMINHO_PASTA) and len(os.listdir(CAMINHO_PASTA)) > 0

Só retorna verdadeiro se as duas forem verdadeiras.


---

🔹 or

Uma ou outra condição.

if resposta == "sim" or resposta == "não":


---

🔹 with open()

Abre arquivo com fechamento automático.

with open(caminho, "w", encoding="utf-8") as arquivo:

Vantagem:

Fecha sozinho.


---

🔹 "w"

Modo escrita.

"w"

Significa:

Write → sobrescreve arquivo.


---

🔹 "r"

Modo leitura.

"r"

Read.


---

🔹 encoding="utf-8"

Permite acentos corretamente.


---

🔹 json.dump()

Salva dicionário em JSON.

json.dump(perfil, arquivo)


---

🔹 json.load()

Lê JSON.

json.load(arquivo)


---

🔹 os.path.exists()

Verifica se arquivo existe.

os.path.exists(caminho)


---

🔹 os.makedirs()

Cria pasta.

os.makedirs(CAMINHO_PASTA, exist_ok=True)


---

🔹 exist_ok=True

Não dá erro se já existir.


---

🔹 os.listdir()

Lista arquivos da pasta.

os.listdir(CAMINHO_PASTA)


---

🔹 for

Loop de repetição.

for i, nome in enumerate(perfis, start=1):


---

🔹 enumerate()

Numera automaticamente.

Resultado:

1 - Felipe
2 - João
3 - Ana


---

🔹 start=1

Começa contagem em 1.


---

🔹 .isdigit()

Verifica se digitou número.

if not escolha.isdigit():


---

🔹 int()

Converte texto para número inteiro.

escolha = int(escolha)


---

🔹 exit()

Encerra programa.

exit()


---

🔹 * no import

from financas import *

Significa:

Importa tudo.

⚠️ Mas em projetos maiores é melhor evitar.


---

📌 Palavras-chave que você já está usando como programador de verdade

Você já trabalha com:

estruturas condicionais

loops

persistência de dados

funções

módulos

JSON

arquivos

listas

dicionários


Isso já é base forte de Python 🚀


---




Vou separar por arquivo para ficar como material de estudo de verdade.


---

📂 perfil.py — keywords, métodos e built-ins usados

Esse arquivo trabalha principalmente com arquivos, listas, JSON, loops e validação de entrada.


---

🔹 import os

import os

Biblioteca padrão do Python para sistema operacional.

Usada para:

criar pastas

verificar existência de arquivos

listar arquivos

remover arquivos



---

🔹 import json

import json

Biblioteca para salvar e ler dados em JSON.


---

🔹 variável global

CAMINHO_PASTA = "perfis"

Variável constante usada por várias funções.

Evita repetir texto várias vezes.


---

🔹 os.path.exists()

os.path.exists(CAMINHO_PASTA)

Verifica se pasta ou arquivo existe.

Retorna:

True
False


---

🔹 len()

len(os.listdir(CAMINHO_PASTA))

Conta quantos arquivos existem.


---

🔹 os.listdir()

os.listdir(CAMINHO_PASTA)

Lista tudo dentro da pasta.

Exemplo:

["Felipe.json", "Ana.json"]


---

🔹 Função com retorno booleano

def perfil_existe():
    return ...

return

Retorna diretamente o resultado lógico.


---

🔹 while True

while True:

Loop infinito usado para repetir até entrada válida.


---

🔹 .strip()

nome.strip()

Remove espaços.


---

🔹 comparação

if len(nome) < 3:

Operador <

Menor que.


---

🔹 operador >

if len(nome) > 60:

Maior que.


---

🔹 continue

continue

Volta para o começo do loop.


---

🔹 break

break

Sai do loop.


---

🔹 os.makedirs()

os.makedirs(CAMINHO_PASTA, exist_ok=True)

Cria pasta.


---

🔹 exist_ok=True

Se já existir, não gera erro.


---

🔹 f-string em caminho

f"{CAMINHO_PASTA}/{nome}.json"

Insere variável dentro do texto.


---

🔹 with open()

with open(caminho, "w", encoding="utf-8") as arquivo:

Abre arquivo com fechamento automático.


---

🔹 "w"

Modo escrita.


---

🔹 "r"

Modo leitura.


---

🔹 encoding="utf-8"

Permite acentos.


---

🔹 json.dump()

json.dump({"nome": nome}, arquivo, ensure_ascii=False)

Salva dicionário no arquivo.


---

🔹 ensure_ascii=False

Mantém caracteres especiais.

Exemplo:

não
João


---

🔹 json.load()

json.load(arquivo)

Lê JSON e transforma em dicionário.


---

🔹 list comprehension

return [
    arquivo.replace(".json", "")
    for arquivo in arquivos
    if arquivo.endswith(".json")
]

Estrutura avançada:


---

for

Percorre lista.


---

if

Filtra elementos.


---

.replace()

arquivo.replace(".json", "")

Remove parte do texto.


---

.endswith()

arquivo.endswith(".json")

Verifica final da string.


---

🔹 enumerate()

for i, nome in enumerate(perfis, start=1):

Numera automaticamente.


---

🔹 start=1

Começa em 1.


---

🔹 .isdigit()

if not escolha.isdigit():

Verifica se digitou número.


---

🔹 int()

escolha = int(escolha)

Converte texto em número.


---

🔹 os.remove()

os.remove(...)

Remove arquivo.


---

🔹 .lower()

confirmacao.lower()

Converte para minúsculo.


---

📂 app.py — recursos usados


---

🔹 imports múltiplos

from perfil import ...

Importa funções específicas.


---

🔹 from financas import *

from financas import *

Importa tudo.

⚠️ Funciona, mas em projetos maiores é melhor evitar.


---

🔹 dicionário

perfil["nome"]

Acessa chave do dicionário.


---

🔹 operador in

if "conhecimento_financeiro" in perfil:

Verifica se chave existe.


---

🔹 input().lower()

input(...).lower()

Recebe texto e já converte.


---

🔹 comparação múltipla com or

if resposta == "sim" or resposta == "não":


---

🔹 return

Usado para sair de função/menu.


---

🔹 exit()

Encerra programa.


---

📂 database.py — principais elementos usados

(considerando a estrutura normal do seu projeto)


---

🔹 import sqlite3

import sqlite3

Biblioteca do banco SQLite.


---

🔹 conexão

sqlite3.connect(...)

Abre banco.


---

🔹 cursor

cursor = conn.cursor()

Objeto que executa comandos SQL.


---

🔹 .execute()

cursor.execute(...)

Executa SQL.


---

🔹 .commit()

conn.commit()

Salva alterações.


---

🔹 .close()

conn.close()

Fecha conexão.


---

📂 financas.py — recursos comuns


---

🔹 SQL INSERT

INSERT INTO

Adiciona dados.


---

🔹 SQL DELETE

DELETE FROM

Remove dados.


---

🔹 SQL SELECT

SELECT

Consulta dados.


---

🔹 agregação

SUM(valor)

Soma valores.


---

🔹 parâmetros SQL seguros

cursor.execute("...", (valor,))

Evita erro e SQL injection.


---

📂 importador_csv.py


---

🔹 import csv

import csv

Biblioteca CSV.


---

🔹 csv.reader()

Lê linhas.


---

🔹 for linha in leitor

Percorre cada linha.


---

🔹 split automático por coluna

CSV já separa:

data,descricao,valor


---

🔹 float()

float(valor)

Converte texto em decimal.


---

📘 Resumo de categorias que você já usa


---

Keywords

if

elif

else

while

for

return

break

continue

import

def

with

in

not

or

and



---

Built-in functions

print()

input()

len()

int()

float()

enumerate()



---

Métodos de string

.strip()

.lower()

.replace()

.endswith()

.isdigit()



---

Bibliotecas usadas

os

json

sqlite3

csv



---

🧠 Dica de estudo forte

Sempre classifique assim:

len() → built-in
.lower() → método
if → keyword
json.dump() → função de biblioteca

📘 Dica profissional de anotação

Quando estudar, divida assim:

keyword

built-in function

método

biblioteca

Exemplo:

len() = built-in
.lower() = método de string
if = keyword
json.dump = função da biblioteca json