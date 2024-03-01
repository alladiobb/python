class Singleton:
    _instance = None

    #Tendo o método com @Ano abaixo ele vai
    #Método chamado antes do __init__ durante a criacão do objeto
    def __new__(cls):
        #verifica se já está defindo
        if not cls._instance:
            #caso não ele cria uma nova instancia 
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        pass


def singleton(cls):
    instances = {}
    def get_instances(*args, **kwargs):
    #def get_instances():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            #instances[cls] = cls()
        return instances[cls]
    return get_instances

@singleton
class Singleton_2:
    def __init__(self):
        # Inicialize a instância aqui
        pass

inst1 = Singleton_2()
inst2 = Singleton_2()
print(inst1 is inst2)


inst1 = Singleton()
inst2 = Singleton()
print(inst1 is inst2)