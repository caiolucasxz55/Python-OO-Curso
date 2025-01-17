class Restaurante():
    restaurantes = []
    
    
    def __init__(self,nome,categoria,premios,avaliação):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.premios = int(premios)
        self.avaliação = float(avaliação)
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome}|{self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}|{restaurante.categoria}|{restaurante.ativo}|{restaurante.premios}|{restaurante.avaliação}')
            
    
          
restaurante_hiro = Restaurante('hiro','sushi','0','4.7')
restaurante_v2 = Restaurante('v2','gastronomia molecular','1','4.9')

Restaurante.listar_restaurantes()