# Sistema de Cadastro de Usuários (CLI)

Projeto feito em Python para praticar lógica de programação e manipulação de arquivos. É um sistema simples de terminal onde dá pra cadastrar usuário, fazer login, remover conta e ver a lista de quem já se cadastrou.

Fiz esse projeto estudando ADS na Estácio, como forma de praticar o que venho aprendendo.

## O que o programa faz

- Cadastra usuário (email, nome de usuário e senha)
- Faz login
- Remove a conta (pede confirmação antes)
- Mostra a lista de usuários cadastrados
- Salva tudo em um arquivo JSON
- A senha não fica salva "pura" no arquivo, ela passa por um hash (SHA-256) antes de salvar

## Bibliotecas usadas

- hashlib (pra fazer o hash da senha)
- json (pra salvar/ler os dados)
- os (limpar o terminal)
- time (pra fazer a barrinha de progresso)
- stdiomask (pra esconder a senha digitada no terminal)

## Como rodar

Precisa instalar uma biblioteca que não é nativa do Python:

```
pip install stdiomask
```

Depois só rodar o arquivo:

```
python main.py
```

Obs: o caminho do arquivo json (variável `caminho`) tá fixo pro meu computador (Windows), então se for testar troca esse caminho pra um da sua máquina, ou só deixa `cadastros.json` mesmo (sem o caminho completo).

## Menu do programa

```
==============================
          XYZ CORP
==============================
|1| - Cadastrar
|2| - Remover
|3| - Logar
|4| - Usuarios
|0| - Sair
```

## Coisas que sei que podem melhorar

- Trocar o caminho fixo do JSON por um caminho relativo
- Colocar "salt" no hash da senha (mais seguro)
- Talvez usar um banco de dados de verdade (SQLite) em vez de JSON
- Validar o email de um jeito melhor (hoje só checa se tem "@" e ".com")
- Separar o código em mais de um arquivo

## Autor

Jhon - estudante de ADS, ainda aprendendo :)
