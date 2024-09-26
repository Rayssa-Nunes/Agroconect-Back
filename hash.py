import hashlib
def gera_senha_hash(senha):
    senha = senha.encode('utf-8')
    return hashlib.sha256(senha).hexdigest()

def verifica_senha_hash(senha, senha_informada):
    senha_informada = senha_informada.encode('utf-8')
    hash_senha_informada = hashlib.sha256(senha_informada).hexdigest()
    return senha == hash_senha_informada

