from django.urls import path
from AppCuentos import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("cuentos/", views.mostrar_cuentos, name="MostrarCuentos"),
    path("sobre_nosotros/", views.sobre_nosotros, name="SobreNosotros"),
    path("agregar_cuento/", views.agregar_cuento, name="AgregarCuento"),
    path("miscuentos/", views.mis_cuentos, name="MisCuentos"),
    path('borrar/<int:pk>/', views.eliminar_cuento, name='BorrarCuento'),

    #Crud cuentos++w
    path("ListaCuentos/", views.cuentos_list.as_view(), name="ListaCuentos"),
    path('cuento/crear/', views.cuentos_create.as_view(), name='New'),
    path('cuento/<int:pk>/', views.cuentos_detalle.as_view(), name='DetalleCuento'),
    path('cuento/editar/<int:pk>/', views.cuentos_update.as_view(), name='EditarCuento'),
    path('cuento/eliminar/<int:pk>/', views.cuentos_delete.as_view(), name='EliminarCuento'),

    # SCRUM Historia
    path('historias/', views.ListaHistorias.as_view(), name='lista_historias'),
    path('historias/nueva/', views.CrearHistoria.as_view(), name='crear_historia'),
    path('historias/<int:pk>/', views.DetalleHistoria.as_view(), name='detalle_historia'),
    path('historias/editar/<int:pk>/', views.ActualizarHistoria.as_view(), name='actualizar_historia'),
    path('historias/eliminar/<int:pk>/', views.EliminarHistoria.as_view(), name='eliminar_historia'),

]
