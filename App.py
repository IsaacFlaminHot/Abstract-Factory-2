from flask import Flask, render_template, request, jsonify
from abc import ABC, abstractmethod

#Productos abstractos
class PlatoFuerte(ABC):
    @abstractmethod
    def servir(self):
        pass

class Bebida(ABC):
    @abstractmethod
    def servir(self):
        pass

class Postre(ABC):
    @abstractmethod
    def servir(self):
        pass


#Productos concretos (Familia de productos 1: Comida Japonesa)
class Ramen(PlatoFuerte):
    def servir(self):
        return "Ramen"
class Sake(Bebida):
    def servir(self):
        return "Sake"
class Dango(Postre):
    def servir(self):
        return "Dango"

#Productos concretos (Familia de productos 2: Comida Mexicana)
class Tacos(PlatoFuerte):
    def servir(self):
        return "Tacos de carne asada"
class AguaJamaica(Bebida):
    def servir(self):
        return "Agua de Jamaica"
class Pastel(Postre):
    def servir(self):
        return "Pastel de tres leches"

#Productos concretos (Familia de productos 3: Comida China)
class ChowMein(PlatoFuerte):
    def servir(self):
        return "Chow Mein"
class TeJazmin(Bebida):
    def servir(self):
        return "Té Jazmín"
class RollitoDulce(Postre):
    def servir(self):
        return "Rollito Dulce con nieve"

#Productos concretos (Familia de productos 4: Comida italiana)
class Pizza(PlatoFuerte):
    def servir(self):
        return "Pizza Margherita"
class Vino(Bebida):
    def servir(self):
        return "Vino Tinto"
class Tiramisú(Postre):
    def servir(self):
        return "Tiramisú"

#Productos concretos (Familia de productos 5: Comida Americana)
class Hamburguesa(PlatoFuerte):
    def servir(self):
        return "Hamburguesa"
class Refresco(Bebida):
    def servir(self):
        return "Refresco de cola"
class Brownie(Postre):
    def servir(self):
        return "Brownie con helado"

#Fabrica abstracta
class RestauranteFactory(ABC):
    @abstractmethod
    def crear_plato_fuerte(self) -> PlatoFuerte:
        pass

    @abstractmethod
    def crear_bebida(self) -> Bebida:
        pass

    @abstractmethod
    def crear_postre(self) -> Postre:
        pass

#Fabrica concreta 
class RestauranteChino(RestauranteFactory):
    def crear_plato_fuerte(self) -> PlatoFuerte:
        return ChowMein()

    def crear_bebida(self) -> Bebida:
        return TeJazmin()

    def crear_postre(self) -> Postre:
        return RollitoDulce()

class RestauranteJapones(RestauranteFactory):
    def crear_plato_fuerte(self) -> PlatoFuerte:
        return Ramen()

    def crear_bebida(self) -> Bebida:
        return Sake()

    def crear_postre(self) -> Postre:
        return Dango()

class RestauranteMexicano(RestauranteFactory):
    def crear_plato_fuerte(self) -> PlatoFuerte:
        return Tacos()

    def crear_bebida(self) -> Bebida:
        return AguaJamaica()

    def crear_postre(self) -> Postre:
        return Pastel()

class RestauranteItaliano(RestauranteFactory):
    def crear_plato_fuerte(self) -> PlatoFuerte:
        return Pizza()

    def crear_bebida(self) -> Bebida:
        return Vino()

    def crear_postre(self) -> Postre:
        return Tiramisú()

class RestauranteAmericano(RestauranteFactory):
    def crear_plato_fuerte(self) -> PlatoFuerte:
        return Hamburguesa()

    def crear_bebida(self) -> Bebida:
        return Refresco()

    def crear_postre(self) -> Postre:
        return Brownie()

# -- Cliente -- 

class Cliente:
    #-- Fabrica por constructuro sin asignar#
    def __init__(self, restaurante: RestauranteFactory):
        self.restaurante = restaurante
        self.plato_fuerte = None
        self.bebida = None
        self.postre = None

    #Metodo para el menu completo#
    def generar_menu(self):
        self.plato_fuerte = self.restaurante.crear_plato_fuerte()
        self.bebida = self.restaurante.crear_bebida()
        self.postre = self.restaurante.crear_postre()

    def servir_comida(self):
        if not self.plato_fuerte:
            self.generar_menu()

        print("Servicio en curso:")
        print(f"Plato fuerte: {self.plato_fuerte.servir()}")
        print(f"Bebida: {self.bebida.servir()}")
        print(f"Postre: {self.postre.servir()}")    

    def cambiar_restaurante(self, nuevo_restaurante: RestauranteFactory):
        print(f"Cambiando restaurante")
        self.restaurante = nuevo_restaurante
        self.generar_menu()

app = Flask(__name__)

diccionario_fabricas = {
    "mexicano": RestauranteMexicano,
    "japones": RestauranteJapones,
    "chino": RestauranteChino,
    "italiano": RestauranteItaliano,
    "americano": RestauranteAmericano
}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ordenar', methods=['POST'])
def ordenar():
    datos = request.get_json()
    tipo_solicitado = datos.get('cocina')

    if tipo_solicitado in diccionario_fabricas:
        fabrica_seleccionada = diccionario_fabricas[tipo_solicitado]()
        cliente = Cliente(fabrica_seleccionada)
        cliente.generar_menu()

        resppuesta = {
            "plato": cliente.plato_fuerte.servir(),
            "bebida": cliente.bebida.servir(),
            "postre": cliente.postre.servir()
        }

        return jsonify(resppuesta)
    else:
        return jsonify({"error": "Tipo de cocina no reconocido"}), 400

if __name__ == '__main__':
    app.run(debug=True)


