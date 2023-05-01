from django.shortcuts import get_object_or_404,render
from .models import Producto, Categoria
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')
    lista_categoria= Categoria.objects.all()
    print(product_list)
    print(lista_categoria)
    context = {
        'product_list': product_list,
        'categorias': lista_categoria
        }
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk= producto_id)
    return render(request,'producto.html', {'producto': producto})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk = categoria_id)
    lista_productos = categoria.producto_set.all()
    lista_categoria= Categoria.objects.all()
    
    context = {
        'productos': lista_productos,
        'categorias': lista_categoria,
        'categoria': categoria
    }
    return render(request,'index.html', context)

def mostrarCat(request):
    # Lógica para obtener la variable show_row
    return render(request, 'layout.html',{'show_row': False})