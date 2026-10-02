from django.shortcuts import render

# Create your views here.
def v1_app2(request):
    # Lista de diccionarios que representan objetos de datos
    lista_elementos = [
            {
                'id': 1,
                'nombre': 'Xioami 17',
                'precio': 900,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/xioami17.png',
                'clase_boton': 'btn-outline-primary',
            },
            {
                'id': 2,
                'nombre': 'Monitor Acer',
                'precio': 250,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/monitor.png',
                'clase_boton': 'btn-outline-success',
            },
            {
                'id': 3,
                'nombre': 'Audífonos Logitech',
                'precio': 60,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/audifonos.png',
                'clase_boton': 'btn-outline-secondary',
            },
    ]

    contexto = {
        'titulo': 'Catálogo de Productos - App 2',
        'lista_elementos': lista_elementos,
    }
    
    return render(request, 'app2/app2.html', contexto)