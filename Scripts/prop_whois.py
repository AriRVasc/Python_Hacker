import whois

dominio = input("Digite o alvo:")
consulta_whois = whois.whois(dominio)

print(consulta_whois.text)
