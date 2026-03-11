from abc import ABC, abstractmethod

#Fabrica abstracta

class ComidaFactory(ABC):
    @abstractmethod
    def crear_comida(self):
        pass


#Productos abstractos
class ChinaFactory(ComidaFactory):
    def crear_comida(self):
        return "Comida China creada"

class JaponesFactory(ComidaFactory):
    def crear_comida(self):
        return "Comida Japonesa creada"

class MexicanaFactory(ComidaFactory):
    def crear_comida(self):
        return "Comida Mexicana creada"

class VietnamitaFactory(ComidaFactory):
    def crear_comida(self):
        return "Comida Vietnamita creada"

class ItalianaFactory(ComidaFactory):
    def crear_comida(self):
        return "Comida Italiana creada"

class Platofuerte

