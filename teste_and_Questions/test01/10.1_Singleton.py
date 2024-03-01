def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class Singleton:
    def __init__(self):
        # Inicialize a instância aqui
        pass

# Uso
instance1 = Singleton()
instance2 = Singleton()

# instance1 e instance2 referenciarão o mesmo objeto
print(instance1 is instance2)  # Saída: True