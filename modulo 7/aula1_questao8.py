def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto
    
    # Verifica o primeiro dígito verificador
    if digito_verif_1 != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto
    
    # Verifica o segundo dígito verificador
    if digito_verif_2 != int(cpf[10]):
        return False
    
    return True

# Função para formatar o CPF para a entrada XXX.XXX.XXX-XX
def formata_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função principal para receber o CPF do usuário e validar
def main():
    cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ").strip()
    
    # Remove caracteres não numéricos e formata o CPF
    cpf_numerico = ''.join(filter(str.isdigit, cpf))
    
    if valida_cpf(cpf_numerico):
        print(f"CPF {formata_cpf(cpf_numerico)} é válido.")
    else:
        print(f"CPF {formata_cpf(cpf_numerico)} é inválido.")

# Executa o programa principal
if __name__ == "__main__":
    main()
