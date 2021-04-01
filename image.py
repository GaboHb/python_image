from PIL import Image
import os

size = (300,300)

def proceso():
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            i.thumbnail(size)
            i.save('reducidas/{}{}'.format(fn, fext))
            


print("OPCIONES PARA REDUCIR LA IMAGEN")
print("1. 800x600 px")
print("2. 400x300 px")
print("3. 200x150 px")

opcion= input ("ELIJA UNA OPCION: ")
opcion = int (opcion)

if opcion == 1:
    size = (800, 600)
    proceso ()
elif opcion == 2:
    size = (400, 300)
    proceso ()
elif opcion == 3:
    size = (200, 150)
    proceso ()

print("IMAGENES GUARDADAS")