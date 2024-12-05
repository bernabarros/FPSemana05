class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def adicionar_stock(self,quantidade):
        self.quantidade = self.quantidade + quantidade
        if quantidade > 0:
            print("1")
        else:
            print("0")
    def vender(self,quantidade):
        if quantidade <= self.quantidade:
            self.quantidade = self.quantidade - quantidade
            print("1")
        else:
            print("0")
    def exibir_info(self):
        print(self.nome,float(self.preco),int(self.quantidade))
    
produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()