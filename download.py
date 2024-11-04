
import pyperclip
import re

# Obtém o texto copiado da área de transferência
phone_number = pyperclip.paste()

# Remove caracteres como parênteses, traços e espaços
cleaned_number = re.sub(r'[\(\)\-\s]', '', phone_number)

# Verifica se o número contém apenas dígitos e tem o comprimento esperado (por exemplo, 10 ou 11 dígitos para um número brasileiro)
if cleaned_number.isdigit() and (11 <= len(cleaned_number) <= 12):
    print(f"Número de telefone válido: {cleaned_number}")
else:
    print("Número de telefone inválido")
