import hashlib
import base64

# SERVIDOR PEDE A SENHA DO USUÁRIO
hash_escolhido = input("Digite o HASH escolhido \nDigite (1): md5 \nDigite (2): SHA-1 \nDigite (3): SHA-256 \nDigite (4): SHA-512 \nDigite (5): Base64 \nDigite: ").lower()
palavra_escolhida = input("Digite a palavra escolhida: ")

if hash_escolhido == "1":
    confirmacao_2 = palavra_escolhida.encode("utf-8")
    help_1 = hashlib.md5(confirmacao_2).hexdigest()
    print(help_1)
elif hash_escolhido == "2":
    confirmacao_2 = palavra_escolhida.encode("utf-8")
    help_2 = hashlib.sha1(confirmacao_2).hexdigest()
    print(help_2)
elif hash_escolhido == "3":
    confirmacao_2 = palavra_escolhida.encode("utf-8")
    help_3 = hashlib.sha256(confirmacao_2).hexdigest()
    print(help_3)
elif hash_escolhido == "4":
    confirmacao_2 = palavra_escolhida.encode("utf-8")
    help_4 = hashlib.sha3_512(confirmacao_2).hexdigest()
    print(help_4)
elif hash_escolhido == "5":
    hash_bytes = palavra_escolhida.encode("utf-8")
    bytes_base64 = base64.b64encode(hash_bytes)
    print(bytes_base64)
    decode = input("Deseja usar o decode BASE64: (Sim ou Não): ").lower()
    if decode == "sim":
        bytes_cripto = bytes_base64.decode("utf-8")
        bytes_revelados = base64.b64decode(bytes_cripto)
        palavra_revelada = bytes_revelados.decode("utf-8")
        print(f"Fora do Base64: {palavra_revelada}")
else:
    print("Combinações erradas.")

