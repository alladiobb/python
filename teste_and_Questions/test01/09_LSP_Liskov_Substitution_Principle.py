#O LSP (Liskov Substitution Principle) é um dos cinco princípios SOLID da programação orientada a objetos (POO). 
#LSP -> Objetos de classes derivadas devem ser substituíveis por objetos de suas classes bases...
#sem que isso afete o comportamento correto do programa.

#Em outras palavras, se você tem uma variável que espera um objeto de uma classe base,...
#você deve poder substituir esse objeto por um objeto de qualquer classe derivada sem que o código precise ser modificado.

#A resposta para essa questão no caso seria essa:
#Um método de subclasse lançando novas exceções não lançadas pelo méodo da classe base


import math

class Forma:
    def area(self):
        raise NotImplementedError
    
    def perimetro(self):
        raise NotImplementedError
    
class retangulo(Forma):
    def __init__(self, base, altura) -> None:
        super().__init__()
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

#Violação de LSP quando não implementamos todos os métodos da classe
class retangulo(Forma):
    def __init__(self, base:float, altura:float) -> None:
        self.base=base
        self.altura=altura
        super().__init__()
    
    def area(self) -> float:
        return (self.base * self.altura) / 2
    
class circulo(Forma):
    def __init__(self, raio) -> None:
        self.raio = raio
        super().__init__()

    def area(self) -> float:
        return math.pi * self.raio **2
    
    #Violação do princípio de Liskov
    def perimetro(self, raio: float) -> float:
        #errada
        perimetro = raio * 2
        return print(f"perimetro é: {perimetro} ")
        #Correta
        #return 2 * math.pi * self.raio
    
c = circulo(Forma)
c.perimetro(5)