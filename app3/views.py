from django.shortcuts import render

# Create your views here.
def v1_app3(request):
    # Lista de diccionarios que representan objetos de datos
    lista_elementos = [
            {
                'id': 1,
                'nombre': 'Mousepad XL',
                'precio': 20,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/mousepad.png',
                'clase_boton': 'btn-outline-primary',
            },
            {
                'id': 2,
                'nombre': 'Micrófono Gamer',
                'precio': 85,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/microfono.png',
                'clase_boton': 'btn-outline-success',
            },
            {
                'id': 3,
                'nombre': 'Tira Led RGB',
                'precio': 8,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/led.png',
                'clase_boton': 'btn-outline-secondary',
            },
    ]

    contexto = {
        'titulo': 'Catálogo de Productos - App 3',
        'lista_elementos': lista_elementos,
    }
    
    return render(request, 'app3/app3.html', contexto)