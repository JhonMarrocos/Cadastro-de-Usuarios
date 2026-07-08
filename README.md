# Sistema de Cadastro e Login (Terminal)

Projeto feito em Python pra praticar lógica de programação, manipulação de arquivos e um pouco de UI no terminal usando a biblioteca `rich`.

É basicamente um sistema de cadastro de usuários rodando no terminal, com senha criptografada e uma interface bem mais bonita do que o `input()` puro (com painéis, tabelas, barra de loading e mensagens coloridas piscando).

## Funcionalidades

- **Cadastrar** – cria um novo usuário com email, nome de usuário e senha (valida email, usuário duplicado e tamanho mínimo da senha)
- **Remover** – exclui um cadastro existente, pedindo confirmação antes
- **Logar** – autentica um usuário já cadastrado
- **Usuarios** – lista todos os cadastrados em uma tabela

Os dados ficam salvos em um arquivo `lista_de_cadastros.json`, então tudo persiste mesmo depois de fechar o programa.

## Como funciona por baixo dos panos

- As senhas nunca são salvas em texto puro — uso `hashlib` (SHA-256) pra criptografar antes de gravar no JSON
- A digitação da senha fica mascarada no terminal com `stdiomask`
- O caminho do arquivo JSON é montado com `os.path`, então funciona tanto rodando o `.py` direto quanto rodando como executável (`.exe`)
- A interface usa `rich` pra Live updates (barra de loading, textos piscando de alerta/destaque), painéis e tabelas
- `match/case` pra controlar o menu principal

## Tecnologias usadas

- Python 3
- [rich](https://github.com/Textualize/rich) – interface no terminal
- [stdiomask](https://pypi.org/project/stdiomask/) – ocultar senha digitada
- `hashlib`, `json`, `os`, `platform` – bibliotecas nativas do Python

## Como rodar

```bash
pip install rich stdiomask
python nome_do_arquivo.py
```

### Gerar o executável (opcional)

Se quiser rodar sem precisar ter o Python instalado, dá pra gerar um `.exe` com o PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --name "nome do executavel" --icon=cad.ico usuarios.py
```

O executável vai ser gerado dentro da pasta `dist/`.

## Motivação

Fiz esse projeto pra treinar conceitos que uso bastante no curso de ADS: autenticação, persistência de dados, tratamento de erros e organização de código em funções. Foi também minha primeira vez brincando de verdade com a lib `rich` pra deixar um projeto de terminal com uma cara mais profissional.

Ainda dá pra melhorar bastante coisa (tratamento de erros mais robusto, talvez migrar pra um banco de dados de verdade), mas o objetivo aqui foi mesmo praticar o básico com um projeto completo, do início ao fim.
