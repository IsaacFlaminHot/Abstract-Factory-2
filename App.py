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
        return {
            "nombre": "Ramen",
            "descripcion": "Fideos tradicionales japoneses en caldo rico en umami con cerdo chashu y huevo.",
            "tags": ["Fideos", "Umami", "Cerdo"]
        }
class Sake(Bebida):
    def servir(self):
        return {
            "nombre": "Sake",
            "descripcion": "Vino de arroz tradicional japonés servido caliente en taza de cerámica.",
            "tags": ["Arroz", "Fermentado", "Con Alcohol"]
        }
class Dango(Postre):
    def servir(self):
        return {
            "nombre": "Dango",
            "descripcion": "Bolitas dulces y masticables de harina de arroz servidas en un palillo de bambú.",
            "tags": ["Arroz", "Dulce", "Tradicional"]
        }

#Productos concretos (Familia de productos 2: Comida Mexicana)
class Tacos(PlatoFuerte):
    def servir(self):
        return {
            "nombre": "Tacos de carne asada",
            "descripcion": "Tortillas de maíz hechas a mano con jugosa carne asada al carbón, guacamole y salsa.",
            "tags": ["Maíz", "Carne", "Picante"]
        }
class AguaJamaica(Bebida):
    def servir(self):
        return {
            "nombre": "Agua de Jamaica",
            "descripcion": "Infusión fría de flor de jamaica, refrescante y ligeramente endulzada.",
            "tags": ["Refrescante", "Frío", "Sin Alcohol"]
        }
class Pastel(Postre):
    def servir(self):
        return {
            "nombre": "Pastel de tres leches",
            "descripcion": "Bizcocho esponjoso bañado en tres tipos de leche, decorado con durazno y crema.",
            "tags": ["Dulzura Alta", "Lácteos", "Esponjoso"]
        }

#Productos concretos (Familia de productos 3: Comida China)
class ChowMein(PlatoFuerte):
    def servir(self):
        return {
            "nombre": "Chow Mein",
            "descripcion": "Fideos salteados al wok con vegetales frescos, pollo y salsa de soja tradicional.",
            "tags": ["Fideos", "Vegetales", "Wok"]
        }
class TeJazmin(Bebida):
    def servir(self):
        return {
            "nombre": "Té Jazmín",
            "descripcion": "Té verde caliente perfumado con delicadas flores de jazmín, ideal para la digestión.",
            "tags": ["Té Verde", "Caliente", "Digestivo"]
        }
class RollitoDulce(Postre):
    def servir(self):
        return {
            "nombre": "Rollito Dulce con nieve",
            "descripcion": "Delicioso rollito de masa frita crujiente relleno de helado artesanal de vainilla.",
            "tags": ["Frito", "Helado", "Dulzura Alta"]
        }

#Productos concretos (Familia de productos 4: Comida italiana)
class Pizza(PlatoFuerte):
    def servir(self):
        return {
            "nombre": "Pizza Margherita",
            "descripcion": "Masa artesanal al horno de leña con salsa de tomate pomodoro, mozzarella fresca y albahaca.",
            "tags": ["Horno de Leña", "Queso", "Tradicional"]
        }
class Vino(Bebida):
    def servir(self):
        return {
            "nombre": "Vino Tinto",
            "descripcion": "Copa de vino tinto reserva, con notas profundas a frutos rojos y madera.",
            "tags": ["Uva", "Cosecha", "Con Alcohol"]
        }
class Tiramisu(Postre):
    def servir(self):
        return {
            "nombre": "Tiramisú",
            "descripcion": "Postre frío de capas de bizcocho bañadas en café espresso y suave crema de mascarpone.",
            "tags": ["Café", "Mascarpone", "Frío"]
        }

#Productos concretos (Familia de productos 5: Comida Americana)
class Hamburguesa(PlatoFuerte):
    def servir(self):
        return {
            "nombre": "Hamburguesa Clásica",
            "descripcion": "Carne de res a la parrilla con queso cheddar derretido, lechuga, tomate y papas fritas.",
            "tags": ["Carne", "Queso", "Parrilla"]
        }
class Refresco(Bebida):
    def servir(self):
        return {
            "nombre": "Refresco de cola",
            "descripcion": "Bebida carbonatada dulce y muy fría, servida en vaso grande con abundantes hielos.",
            "tags": ["Burbujas", "Azúcar", "Frío"]
        }
class Brownie(Postre):
    def servir(self):
        return {
            "nombre": "Brownie con helado",
            "descripcion": "Cuadro de pastel de chocolate denso y caliente, servido con una bola de helado de vainilla.",
            "tags": ["Chocolate", "Caliente y Frío", "Dulzura Alta"]
        }

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
        return Tiramisu()

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

app = Flask(__name__)

diccionario_fabricas = {
    "mexicana": RestauranteMexicano,
    "japonesa": RestauranteJapones,
    "china": RestauranteChino,
    "italiana": RestauranteItaliano,
    "americana": RestauranteAmericano
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

        respuesta = {
            "plato": cliente.plato_fuerte.servir(),
            "bebida": cliente.bebida.servir(),
            "postre": cliente.postre.servir()
        }

        return jsonify(respuesta)
    else:
        return jsonify({"error": "Tipo de cocina no reconocido"}), 400

if __name__ == '__main__':
    app.run(debug=True)


