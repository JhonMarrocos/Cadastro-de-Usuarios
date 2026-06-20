# Bibliotecas Necessarias

from time import sleep as sl
import hashlib
import os
import json
import stdiomask

# VariáVeis Principais

usuarios = {"Emails": [],
            "Usuarios": [],
            "Senhas": []
            }

caminho = r'C:\Users\Marrocos\Desktop\Repositorio CODE\cadastro de usuarios\cadastros.json' # Banco de dados dos cadastrados

# Funções

def limpar(): # Limpa o Terminal
    os.system('cls')

def criptografar_senha(senha): # Criptografa a senhas usando hash
    return hashlib.sha256(senha.encode()).hexdigest()

def Progress(): # Barra de Loading similar ao usando no tqdm
    
    for n in range(101):
        i = "■" * (n * 25 // 101)
        print(f"\r{n}% {i}", end="", flush=True)
        sl(0.01)
    print()

def Titulo(text): # Retorta um Cabeçalho
    linhas = "=" * 30
    return f"{linhas}\n{text.center(len(linhas))}\n{linhas}"

def carregar(): # Carrega os Dados dos usuarios cadastrados
    global usuarios

    try:
        with open(caminho, "r", encoding="utf-8") as arq:
            usuarios = json.load(arq)

    except FileNotFoundError:
        escrever()

def escrever(): # Escreve/Atualiza dados dos usuarios cadastrados
    with open(caminho, "w", encoding="utf-8") as arq:
        json.dump(usuarios, arq, indent=4)

def Main(): # Corpo Principal do Programa

    while True:
        
        print(Titulo("XYZ CORP"))
        Progress()
        print(Titulo("|1| - Cadastrar\n|2| - Remover\n|3| - Logar\n|4| - Usuarios\n|0| - Sair"))
        
        try:
            opc = int(input("Escolha Uma Opcao: "))
            limpar()
            Progress()
            match opc:

                case 1:
                    while True:
                        cad_email = str(input("Digite Seu Email: ")).strip()

                        if not '@' in cad_email or not '.com' in cad_email:
                            print("Email inválido!")
                            continue
                        
                        if cad_email in usuarios["Emails"]:
                            print(f"O Email {cad_email} ja Existe!")
                            continue

                        while True:
                            cad_usuario = str(input("Digite um Nome de Usuario: ")).strip()
                            
                            if cad_usuario in usuarios["Usuarios"]:
                                print(f"O Usuario {cad_usuario} ja esta Cadastrado!")

                            else:
                                break

                        cad_senha = str(input("Escolha uma Senha de no minimo 8 Caracteres: ")).strip()

                        if len(cad_senha) < 8:
                            print(f"A senha {cad_senha} e invalida!")
                            continue

                        else:
                            usuarios["Emails"].append(cad_email)
                            usuarios["Usuarios"].append(cad_usuario)
                            usuarios["Senhas"].append(criptografar_senha(cad_senha))

                            print("Cadastrando...")
                            Progress()
                            print("Cadastro Realizado com Sucesso!")
                            escrever()
                            input('Aperte ENTER para continuar...')
                            limpar()

                        break
                        
                case 2:
                    login = str(input("Usuario: ")).strip()
                    senha = stdiomask.getpass(prompt='Senha: ', mask='*')

                    if login in usuarios["Usuarios"]:
                        idx = usuarios["Usuarios"].index(login)

                        if usuarios["Senhas"][idx] == criptografar_senha(senha):
                        
                            remover = input(
                                "Tem certeza que deseja excluir a conta? S/N: "
                            ).strip().upper()

                            if remover == "S":
                                usuarios["Emails"].pop(idx)
                                usuarios["Usuarios"].pop(idx)
                                usuarios["Senhas"].pop(idx)

                                escrever()
                                print("Usuário removido com sucesso!")

                            elif remover == "N":
                                print("Voltando ao menu...")

                        else:
                            print("Usuario ou Senha Invalida!")

                    else:
                        print("Usuario ou Senha Invalida!")
                    
                    input('Aperte ENTER Para Continuar...')
                    limpar()
                    
                case 3:
                    login = str(input("Usuario: ")).strip()
                    senha = stdiomask.getpass(prompt='Senha: ', mask='*')

                    if login in usuarios["Usuarios"]:
                        idx = usuarios["Usuarios"].index(login)
                        if usuarios["Senhas"][idx] == criptografar_senha(senha):
                            print(f"Bem Vindo {login}!")
                        else:
                            print("Usuario ou Senha Invalida!")
                    else:
                        print("Usuario ou Senha Invalida!")
                    
                    input('Aperte ENTER para continuar...')
                    limpar()
                    continue

                case 4:
                    for i, email in enumerate(usuarios["Emails"]):
                        print(f"|{i+1}| - Nick: {usuarios['Usuarios'][i]} Email: {email}")
                    
                    print()
                    input("Aperte ENTER Para Continuar...")
                    limpar()
                    continue

                case 0:
                    print("Saindo...")
                    Progress()
                    print("Ate Mais!")
                    break

                case _:
                    print("Opcao Invalida!")

        except ValueError:
            print("Digite Somente Numeros!")

# Main

carregar()
Main()