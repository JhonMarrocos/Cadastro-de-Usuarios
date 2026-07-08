# Bibliotecas Necessarias

# Terminal Detalhado ↓
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from rich import print

# Temporizador para Pausa ↓
from time import sleep as sl

# Segurança de Senha ↓
import stdiomask
import hashlib

# Interações com o Sistema ↓
import platform
import sys
import os
import json

# Variáveis Principais

usuarios = []  # Armazena (Email, Usuario, Senha) na variavel usuarios

if getattr(sys, "frozen", False):
    local_arquivo = os.path.dirname(
        sys.executable
    )  # Localiza o diretorio do programa se (execultavel)

else:
    local_arquivo = os.path.dirname(
        os.path.abspath(__file__)
    )  # Localiza o diretorio do programa se (srcipt)

arquivo_json = os.path.join(
    local_arquivo, "lista_de_cadastros.json"
)  # Banco de dados dos cadastrados

# Funções


def limpar():  # Limpa o Terminal

    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")


def continuar():  # Pausa o terminal ate que o usuário pressione ENTER
    Prompt.ask("[cyan]ENTER[/] para continuar")
    limpar()


def loading():  # Barra de Loading similar ao usando no tqdm
    with Live("", refresh_per_second=30) as live:
        for n in range(101):
            i = "■" * (n * 25 // 101)
            if n < 33:
                live.update(f"|{n}%|[[red]{i}[/]]")

            else:
                live.update(f"|{n}%|[[yellow]{i}[/]]")

            sl(0.01)
        live.update(f"|{n}%|[[rgb(0,255,0)]{i}[/]]")


def cor_destaque(texto):  # Converte um Texto em uma msg em destaque piscando em verde
    with Live("", refresh_per_second=20) as live:
        cores = ["[rgb(0,85,0)]", "[rgb(0,170,0)]", "[rgb(0,255,0)]"]
        for i in range(5):
            for cor in cores:
                live.update(f"{cor}{texto}[/]")
                sl(0.1)


def cor_alerta(texto):  # Converte um Texto em uma msg de alerta piscando em vermelho
    with Live("", refresh_per_second=20) as live:
        cores = ["[rgb(85,0,0)]", "[rgb(170,0,0)]", "[rgb(255,0,0)]"]
        for i in range(10):
            for cor in cores:
                live.update(f"{cor}{texto}[/]")
                sl(0.05)


def encontrar_email(email):  # Verifica se existe o email na lista de usuarios
    for i, item in enumerate(usuarios):
        if item["Email"] == email:
            return i
    return -1


def encontrar_usuario(usuario):  # Verifica se existe o usuario na lista de usuarios
    for i, item in enumerate(usuarios):
        if item["Usuario"] == usuario:
            return i
    return -1


def criptografar_senha(senha):  # Criptografa a senhas usando hash

    return hashlib.sha256(senha.encode()).hexdigest()


def carregar():  # Carrega os Dados dos usuarios cadastrados

    global usuarios

    try:
        with open(arquivo_json, "r", encoding="utf-8") as arq:
            usuarios = json.load(arq)

    except FileNotFoundError:
        escrever()


def escrever():  # Escreve/Atualiza dados dos usuarios cadastrados

    with open(arquivo_json, "w", encoding="utf-8") as arq:
        json.dump(usuarios, arq, indent=4, ensure_ascii=False)


def menu():  # Menu Principal Interativo
    print(
        Panel(
            """|[rgb(0,255,255)]1[/]| - [white]Cadastrar[/]\n|[rgb(0,255,255)]2[/]| - [white]Remover[/]\n|[rgb(0,255,255)]3[/]| - [white]Logar[/]\n|[rgb(0,255,255)]4[/]| - [white]Usuarios[/]\n|[red]0[/]| - [red]Sair[/]""",
            title="[red]X[/][green]Y[/][blue bold]Z[/] [white]Corporation[/]",
            style="rgb(210,180,120)",
            width=30,
        )
    )

    opcao = int(input("\nEscolha Uma Opcao: "))
    return opcao


def cadastrar():  # Opção [1] do menu (Cadastrar)
    while True:
        email = str(input("Digite Seu Email: ")).strip()
        limpar()

        if (
            "@gmail.com" not in email
            and "@hotmail.com" not in email
            and "@outlook.com" not in email
        ):
            print("Email inválido!")
            continuar()
            continue

        indice = encontrar_email(email)

        if indice != -1:
            print(f"O Email {email} ja Existe!")
            continuar()
            continue

        while True:
            usuario = str(input("Digite um Nome de Usuario: ")).strip()
            limpar()

            indice = encontrar_usuario(usuario)
            if not usuario:
                limpar()
                continue

            if indice != -1:
                print(f"O Usuario {usuario} ja esta Cadastrado!")
                continuar()

            else:
                break

        while True:
            senha = str(input("Escolha uma Senha de no minimo 8 Caracteres: ")).strip()
            limpar()

            if not senha:
                continue

            if len(senha) < 8:
                cor_alerta(f"[white]A senha[/] [green]{senha}[/] [white]e[/] invalida!")
                continuar()
                continue

            else:
                usuarios.append(
                    {
                        "Email": email,
                        "Usuario": usuario,
                        "Senha": criptografar_senha(senha),
                    }
                )

                print("Cadastrando...")
                loading()
                print("[white]Cadastro Realizado com[/] [cyan]Sucesso[/]!")
                escrever()
                continuar()
            break
        break


def remover():  # Opção [2] do menu (Remover)
    if not usuarios:
        cor_alerta("[white]Lista de Cadastrados[/] Vazia!")
        continuar()
        return

    while True:
        login = str(input("Usuario: ")).strip()
        if not login:
            limpar()
            continue
        break

    senha = stdiomask.getpass(prompt="Senha: ", mask="*")
    limpar()

    idx = encontrar_usuario(login)

    if idx != -1 and usuarios[idx]["Senha"] == criptografar_senha(senha):
        remover = (
            input("Tem certeza que deseja excluir a conta? ([S] || [N]): ")
            .strip()
            .upper()
        )
        limpar()

        if remover == "S":
            usuarios.pop(idx)
            escrever()
            cor_destaque(
                f"[white]Usuário[/] {login} [white]removido com [cyan]sucesso[/][white]![/]"
            )
            continuar()
        elif remover == "N":
            print("Voltando ao menu...")
            loading()

    else:
        print("Usuario ou Senha Invalida!")
        continuar()


def logar():  # Opção [3] do menu (Logar)
    if not usuarios:
        cor_alerta("[white]Lista de Cadastrados[/] Vazia!")
        continuar()
        return

    while True:
        login = str(input("Usuario: ")).strip()
        if not login:
            limpar()
            continue
        break

    senha = stdiomask.getpass(prompt="Senha: ", mask="*")
    limpar()

    idx = encontrar_usuario(login)

    if idx != -1 and usuarios[idx]["Senha"] == criptografar_senha(senha):
        print(f"[cyan]Seja Bem Vindo[/]! [green]{login.upper()}[/]")
        continuar()

    else:
        print("Usuario ou Senha Invalida!")
        continuar()
    return


def cadastrados():  # opção [4] do menu (Usuarios)
    if not usuarios:
        cor_alerta("[white]Lista de Cadastrados[/] Vazia!")
        continuar()
        return

    console = Console()
    tabela = Table(title="[white]Usuarios[/]", style="rgb(210,180,120)")

    tabela.add_column("[red]ID[/]", justify="center")
    tabela.add_column("[green]Usuários[/]", justify="center")
    tabela.add_column("[blue]Emails[/]", justify="center")

    for i, item in enumerate(usuarios):
        tabela.add_row(
            f"[cyan]{i}[/]",
            f"[white]{item['Usuario']}[/]",
            f"[white]{item['Email']}[/]",
        )

    console.print(tabela)

    print()
    continuar()
    return


# main (corpo principal do programa)

limpar()
print("Iniciando...")
loading()
sl(1)
limpar()
carregar()

while True:
    try:
        opc = menu()
        limpar()

        match opc:
            case 1:
                cadastrar()

            case 2:
                remover()

            case 3:
                logar()

            case 4:
                cadastrados()

            case 0:  # Opção [0] do menu (Sair)
                print("Saindo...")

                with Live("", refresh_per_second=20) as live:
                    tchau = [":hand:", ":wave:"]
                    for v in range(3):
                        for i in tchau:
                            live.update(f"Ate Mais!{i}")
                            sl(0.3)
                break

            case _:
                cor_alerta(f"[white]A Opção[/] [cyan]{opc}[/] não existe!")
                continuar()

    except ValueError as erro:
        limpar()
        cor_alerta(
            f"[cyan]Digite Somente uma das Opções Apresentadas![/]\n[yellow]Erro:[/] {erro}"
        )
        continuar()