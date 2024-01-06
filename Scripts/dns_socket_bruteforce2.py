import socket
import os

dominio = input("Digite o alvo:")

# Verifica se o arquivo existe antes de abri-lo
arquivo_path = "Scripts/brute.txt"
if os.path.exists(arquivo_path):
    with open(arquivo_path, "r") as arquivo:
        bruteforce = arquivo.readlines()

    for nome in bruteforce:
        DNS = nome.strip() + "." + dominio  # Remova espaços em branco, incluindo a nova linha
        try:
            print(DNS + ": " + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass
else:
    print(f"O arquivo {arquivo_path} não foi encontrado.")
