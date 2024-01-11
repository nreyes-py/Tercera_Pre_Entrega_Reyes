from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppCuentos.forms import CuentoForm, HistoriaForm
from .models import Cuento, Perfil, Historia


def perfil_usuario(request, usuario_id):
#     perfil = Perfil.objects.get(usuario_id=usuario_id)
#     cuentos = Cuento.objects.filter(autor=perfil.usuario)
    return render(request, 'AppCuentos/perfil_usuario.html')



def historias_comunes(request):
    # Puede ser simplemente una página estática
    return render(request, 'AppCuentos/mis_cuentos.html')


def inicio(request):
    return render(request, 'AppCuentos/inicio.html')

def mostrar_cuentos(request):
    cuentos = Cuento.objects.all()
    contexto = {"cuentos":cuentos}
    return render(request, 'AppCuentos/mostrar_cuentos.html', contexto)
    # return render(request, 'AppCuentos/mostrar_cuentos.html')

def mis_cuentos(request):
      cuentos = Cuento.objects.all() 
      contexto= {"cuentos":cuentos} 
      return render(request, "AppCuentos/mis_cuentos.html", contexto)



def sobre_nosotros(request):
    # Puede ser simplemente una página estática
    return render(request, 'AppCuentos/sobre_nosotros.html')


def detalle_cuento(request):
    cuento = Cuento.objects.get(all)
    contexto = {"detallecuento":cuento}
    return render(request, 'AppCuentos/detalle_cuento.html',  contexto)


def agregar_cuento(request):
    if request.method == 'POST':

        miCuento = CuentoForm(request.POST)

        if miCuento.is_valid():
            informacion = miCuento.cleaned_data
            cuento = Cuento(autor=informacion["autor"], titulo=informacion["titulo"], contenido=informacion["contenido"], puntuacion=informacion["puntuacion"])
            cuento.save()
            cuentos = Cuento.objects.all() 
            contexto= {"cuentos":cuentos} 
            return render(request, 'AppCuentos/mis_cuentos.html', contexto)  # Redirige a la página principal después de guardar
    else:
        miCuento = CuentoForm()

    return render(request, 'AppCuentos/agregar_cuento.html',{"cuento1":miCuento})

def eliminar_cuento(request, titulo):
    cuento = Cuento.objects.get(titulo="titulo")
    cuento.delete()
    cuento = Cuento.objects.all()
    contexto = {"cuentos":cuento}
    return render(request, 'AppCuentos/mostrar_cuentos.html',  contexto)

class cuentos_list(ListView):
    model = Cuento
    template_name ="AppCuentos/cuento_list.html"

class cuentos_detalle(DetailView):
    model = Cuento
    template_name ="AppCuentos/detalle_cuento.html"

class cuentos_create(CreateView):
    model = Cuento
    success_url = "/AppCuentos/ListaCuentos/"
    fields  = ["autor","titulo","contenido","puntuacion"]

class cuentos_update(UpdateView):
    model = Cuento
    success_url = "/AppCuentos/ListaCuentos/"
    fields  = ["autor","titulo","contenido","puntuacion"]
    
class cuentos_delete(DeleteView):
    model = Cuento
    success_url =  "/AppCuentos/ListaCuentos/"


    # return render(request, 'AppCuentos/detalle_cuentos.html')

# Scrum Historias
class ListaHistorias(ListView):
    model = Historia
    template_name = 'AppCuentos/historia_list.html'

class DetalleHistoria(DetailView):
    model = Historia
    template_name = 'AppCuentos/historia_detail.html'

class CrearHistoria(CreateView):
    model = Historia
    success_url = "/AppCuentos/historias/"
    fields  = ["autor","titulo","contenido","puntuacion"]


class ActualizarHistoria(UpdateView):
    model = Historia
    # template_name = 'AppCuentos/actualizar_historia.html'
    success_url = "/AppCuentos/historias/"
    fields  = ["autor","titulo","contenido","puntuacion"]

class EliminarHistoria(DeleteView):
    model = Historia
    # template_name = 'AppCuentos/eliminar_historia.html'
    success_url = "/AppCuentos/historias/"
