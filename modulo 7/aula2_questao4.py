import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    if not (tem_maiuscula and tem_minuscula):
        return False

    tem_numero = any(c.isdigit() for c in senha)
    if not tem_numero:
        return False
    
    tem_especial = re.search(r'[!@#$%^&*()_+{}":?><,./;\'\[\]\\|=]', senha)
    if not tem_especial:
        return False
    
    return True

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  
print(validador_senha(senha2))  
print(validador_senha(senha3))
