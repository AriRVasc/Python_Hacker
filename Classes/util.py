class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        

    def printar_nome_completo(self):
        return self.nome + " " + self.sobrenome
    
nomes = ["Afonso", "Maria", "João"]
sobrenomes = ["Padilha", "Silva", "Santos"]

for nome, sobrenome in zip(nomes, sobrenomes):
    info_pessoa = Pessoa(nome,sobrenome)
    print(info_pessoa.printar_nome_completo())