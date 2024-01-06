import base64
import hashlib

#contar caractere especifico
frase = "Joao e o pe de feijao"
print (frase.count("o"))

# Codificação e decodificação em base64
encrypt = base64.b64encode(frase.encode("utf-8"))
print(encrypt)


decrypt = base64.b64decode(encrypt).decode("utf-8")
print(decrypt)



# Criando um objeto hash SHA-256
texto = "Exemplo de texto para hash SHA-256"

hash_object = hashlib.sha256()

hash_object.update(texto.encode('utf-8'))

hash_hex = hash_object.hexdigest()

print("Texto original:", texto)
print("Hash SHA-256:", hash_hex)


#buscar palavra especifica em texto
texto2 = "Um dia bonito começa com um barril de esperança e um café de otimismo."
print(texto2.find("dia"))
print(texto2.rfind("dia"))
print(texto2.index("dia"))