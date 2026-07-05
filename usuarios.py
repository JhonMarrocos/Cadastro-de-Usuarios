# Bibliotecas Necessarias

# Terminal Detalhado ↓
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

# Temporizador para Pausa ↓
from time import sleep as sl

# Segurança de Senha ↓
import stdiomask
import hashlib

# Interações com o Sistema ↓
import platform
import os
import json

# Variáveis Principais

usuarios = []  # Armazena (Email, Usuario, Senha) na variavel usuarios

local_arquivo = os.path.dirname(
    os.path.abspath(__file__)
)  # Localiza o script do programa

arquivo_json = os.path.join(
    local_arquivo, "cadastros.json"
)  # Banco de dados dos cadastrados

# Funções


def limpar():  # Limpa o Terminal

    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")


def pausar():  # Pausa o terminal
    return Prompt.ask("[cyan]ENTER[/] para continuar")


def loading():  # Barra de Loading similar ao usando no tqdm
    with Live("", refresh_per_second=30) as live:
        for n in range(101):
            i = "■" * (n * 25 // 101)
            if n < 33:
                live.update(f"|{n}%|[red]{i}[/]")

            else:
                live.update(f"|{n}%|[yellow]{i}[/]")

            sl(0.01)
        live.update(f"|{n}%|[green]{i}[/]|")


def cor_alerta(texto):
    with Live("", refresh_per_second=20) as live:
        cores = ["[rgb(85,0,0)]", "[rgb(170,0,0)]", "[rgb(255,0,0)]"]
        vezes = 10
        for i in range(vezes):
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


def main():  # Corpo Principal do Programa
    while True:
        try:
            opc = menu()
            limpar()

            match opc:
                case 1:
                    while True:
                        email = str(input("Digite Seu Email: ")).strip()
                        limpar()

                        if (
                            "@gmail.com" not in email
                            and "@hotmail.com" not in email
                            and "@outlook.com" not in email
                        ):
                            print("Email inválido!")
                            pausar()
                            limpar()
                            continue

                        indice = encontrar_email(email)

                        if indice != -1:
                            print(f"O Email {email} ja Existe!")
                            pausar()
                            limpar()
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
                                pausar()
                                limpar()

                            else:
                                break

                        senha = str(
                            input("Escolha uma Senha de no minimo 8 Caracteres: ")
                        ).strip()
                        limpar()

                        if not senha:
                            continue

                        if len(senha) < 8:
                            print(f"A senha {senha} e invalida!")
                            pausar()
                            limpar()
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
                            print("\nCadastro Realizado com Sucesso!")
                            escrever()
                            pausar()
                            limpar()

                        break

                case 2:
                    if not usuarios:
                        print("Lista de Cadastrados [red]Vazia![/]")
                        pausar()
                        limpar()
                        continue

                    login = str(input("Usuario: ")).strip()
                    senha = stdiomask.getpass(prompt="Senha: ", mask="*")
                    limpar()

                    idx = encontrar_usuario(login)

                    if idx != -1 and usuarios[idx]["Senha"] == criptografar_senha(
                        senha
                    ):
                        remover = (
                            input(
                                "Tem certeza que deseja excluir a conta? ([S] || [N]): "
                            )
                            .strip()
                            .upper()
                        )
                        limpar()

                        if remover == "S":
                            usuarios.pop(idx)
                            escrever()
                            print("Usuário removido com sucesso!")
                            pausar()
                            limpar()

                        elif remover == "N":
                            print("Voltando ao menu...")
                            loading()

                    else:
                        print("Usuario ou Senha Invalida!")
                        pausar()
                        limpar()

                case 3:
                    login = str(input("Usuario: ")).strip()
                    senha = stdiomask.getpass(prompt="Senha: ", mask="*")
                    limpar()

                    idx = encontrar_usuario(login)

                    if idx != -1 and usuarios[idx]["Senha"] == criptografar_senha(
                        senha
                    ):
                        print(f"Bem Vindo {login}!")
                        pausar()
                        limpar()

                    else:
                        print("Usuario ou Senha Invalida!")
                        pausar()
                        limpar()

                    continue

                case 4:
                    for i, item in enumerate(usuarios):
                        print(
                            f"|{i + 1}| - Nick: {item['Usuario']} Email: {item['Email']}"
                        )

                    print()
                    pausar()
                    limpar()
                    continue

                case 0:
                    print("Saindo...")

                    with Live("", refresh_per_second=20) as live:
                        tchau = [":hand:", ":wave:"]
                        for v in range(3):
                            for i in tchau:
                                live.update(f"Ate Mais!{i}")
                                sl(0.3)
                    break

                case _:
                    print("Opcao Invalida!")
                    pausar()
                    limpar()

        except ValueError as erro:
            cor_alerta(erro)
            print("[cyan]Digite Somente Numeros![/]")
            pausar()
            limpar()


# main
limpar()
print("Iniciando...")
loading()
sl(1)
limpar()
carregar()
main()
