from django.shortcuts import render

# Create your views here.
def v1_app1(request):
    # Lista de diccionarios que representan objetos de datos
    lista_elementos = [
            {
                'id': 1,
                'nombre': 'Notebook Lenovo',
                'precio': 750,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/notebook.png',
                'clase_boton': 'btn-outline-primary',
            },
            {
                'id': 2,
                'nombre': 'Mouse Inalámbrico',
                'precio': 45,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/mouse.png',
                'clase_boton': 'btn-outline-success',
            },
            {
                'id': 3,
                'nombre': 'Teclado Mecánico',
                'precio': 60,
                'texto_boton': 'Ver detalles',
                'imagen': 'image/teclado.jpg',
                'clase_boton': 'btn-outline-secondary',
            },
    ]

    contexto = {
        'titulo': 'Catálogo de Productos - App 1',
        'lista_elementos': lista_elementos,
    }
    
    return render(request, 'app1/app1.html', contexto)