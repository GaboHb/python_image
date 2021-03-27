from PIL import Image
imagen = Image.open("images/amapolas.jpg")


def proceso(a, b):
    reducida = imagen.resize((a, b))
    reducida.show()
    reducida.save('images/reducida.jpg')
    print("LA IMAGEN SE HA GUARDADO")

print("OPCIONES PARA REDUCIR LA IMAGEN")
print("1. 800x600 px")
print("2. 400x300 px")
print("3. 200x150 px")

opcion= input ("ELIJA UNA OPCION: ")
opcion = int (opcion)

if opcion == 1:
    proceso (800, 600)
elif opcion == 2:
    proceso (400, 300)
else:
    proceso (200, 150)
