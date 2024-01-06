with open ("arquivo.txt" , "w") as arquivo:
    arquivo.write("Hello World!")
   

with open ("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
