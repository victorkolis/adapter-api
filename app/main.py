# Banco de dados stateless, ou seja, que perde sua memória


banco_de_dados = {}


# TODO: crie uma função que peça, nome, sobrenome, email, senha, confirmar senha
def set_usuarios():
    primeiro_nome = input('Nome: ')

    if len(primeiro_nome) < 3:
        return {'msg': f'Muito curto: {primeiro_nome}'}

    sobrenome = input('Sobrenome: ')
    email = input('E-mail: ') + '@gmail.com'
    senha = input('Senha: ')
    confirmar_senha = input('Confirmar senha: ')


    banco_de_dados['nome'] = primeiro_nome
    banco_de_dados['sobrenome'] = sobrenome
    banco_de_dados['email'] = email
    banco_de_dados['senha'] = senha
    banco_de_dados['confirmar_senha'] = confirmar_senha


print(set_usuarios())
print(banco_de_dados)
