usuario_certo = "edu"
senha_certa = "1234"

tentativas_max = 3


for tentativas in range(tentativas_max):
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == usuario_certo and senha == senha_certa:
        print(f"Bem-vindo, {usuario}")
        break

    else:
        tentativas_restantes = tentativas_max - (tentativas + 1)
        if tentativas_restantes > 0:
            print(f"Usuario ou senha incorretos. Você tem {tentativas_restantes} tentativas restantes antes do acesso ser bloqueado.")
        
        else:
            print(f"Acesso bloqueado.")



        

