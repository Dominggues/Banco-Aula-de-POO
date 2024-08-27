from database import BancoDeDados

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

    #print(banco.login("well","123"))

    #banco.inserir_cliente("well", "123", "11111111111", "wel@gmail.com")
    #banco.inserir_cliente("roque", "321","22222222222", "roque@gmail.com")
    #banco.inserir_cliente("test", "456",'33333333333', 'test@gmail.com')
    #banco.inserir_cliente("eduardo", "123", "66666666666", "eduardo@gmail.com")
    
    #banco.buscar_cliente("66666666666")

    #banco.buscar_email("wel@gmail.com")

    #banco.remover_cliente("11111111111")

    banco.desconecta()