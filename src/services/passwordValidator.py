import string

def validatePassword(password: str) -> tuple[bool, list[str]]:
    caracteres_especiais = string.punctuation
    erros = []
    
    if len(password) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
        
    if not any(char.isupper() for char in password):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
        
    if not any(char.islower() for char in password):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")
        
    if not any(char.isdigit() for char in password):
        erros.append("A senha deve conter pelo menos um dígito numérico.")
        
    if not any(c in caracteres_especiais for c in password):
        erros.append(f"A senha deve conter pelo menos um caractere especial (ex: {caracteres_especiais}).")
        
    if not erros:
        return True, ["Senha forte!"]
    else:
        return False, erros