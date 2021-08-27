
usuario = input("usuario: ")
password = int(input("contraseña: "))

if usuario == "admin" and password == 123456:
    print("Open app")
    peso = int(input("Cuantos kilos pesa el paquete: "))

    def costo_envio(peso):
        if peso == 1:
            return 1.5
        elif peso > 1 and peso < 5:
            return 3
        elif peso >= 5:
            return peso
        
    usd = costo_envio(peso)

    def usd2ars(usd):
        x = usd * 130
        return x

    precio = usd2ars(usd)

    print("el precio por envio es: " + str(precio) + " Pesos ars")
else:
    print("Error en el usuario o contraseña")
