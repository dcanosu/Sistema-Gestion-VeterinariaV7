
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Mascota, Cita
from django.forms import ModelForm
from django import forms 



class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'telefono', 'direccion']

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'propietario']

class CitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'motivo', 'diagnostico', 'mascota']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}), 
        }


def home(request):
    """
    Página de bienvenida
    """
    return render(request, 'vet_sprint/home.html', {'nombre_clinica': 'Clínica Veterinaria Amigos Peludos'})

def services(request):
    """
    Página de servicios
    """
    context = {
        'titulo': 'Nuestros Servicios Veterinarios',
        'servicios_list': [
            'Consultas generales y vacunación',
            'Registros de usuarios y mascotas',
            'Manejo de información de personas y mascotas',
            'Eliminación de usuarios',
            'Gestión de citas' # Servicio adicional
        ],
        'descripcion_adicional': 'Ofrecemos el mejor cuidado para tus mascotas.'
    }
    return render(request, 'vet_sprint/service.html', context)

def dynamic_content_placeholder(request):
    """
    Página con placeholders - Ahora redirige a la lista de propietarios.
    """
    return redirect('propietarios_list')

#gestión de Propietarios
def propietarios_list(request):
    """
    Muestra una lista de todos los propietarios.
    """
    propietarios = Propietario.objects.all()
    return render(request, 'vet_sprint/propietarios_list.html', {'propietarios': propietarios})

def propietario_create(request):
    """
    Permite crear un nuevo propietario.
    """
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietarios_list')
    else:
        form = PropietarioForm()
    return render(request, 'vet_sprint/propietario_form.html', {'form': form, 'accion': 'Crear'})

def propietario_update(request, pk):
    """
    Permite actualizar un propietario existente.
    """
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('propietarios_list')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'vet_sprint/propietario_form.html', {'form': form, 'accion': 'Actualizar'})

def propietario_delete(request, pk):
    """
    Permite eliminar un propietario.
    """
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        propietario.delete()
        return redirect('propietarios_list')
    return render(request, 'vet_sprint/propietario_confirm_delete.html', {'propietario': propietario})

# gestión de Mascotas
def mascotas_list(request):
    """
    Muestra una lista de todas las mascotas.
    """
    mascotas = Mascota.objects.all()
    return render(request, 'vet_sprint/mascotas_list.html', {'mascotas': mascotas})

def mascota_create(request):
    """
    Permite crear una nueva mascota.
    """
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'vet_sprint/mascota_form.html', {'form': form, 'accion': 'Crear'})

def mascota_update(request, pk):
    """
    Permite actualizar una mascota existente.
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'vet_sprint/mascota_form.html', {'form': form, 'accion': 'Actualizar'})

def mascota_delete(request, pk):
    """
    Permite eliminar una mascota.
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas_list')
    return render(request, 'vet_sprint/mascota_confirm_delete.html', {'mascota': mascota})

#Gestión de Cita
def citas_list(request):
    """
    Muestra una lista de todas las citas.
    """
    citas = Cita.objects.all()
    return render(request, 'vet_sprint/citas_list.html', {'citas': citas})

def cita_create(request):
    """
    Permite agendar una nueva cita.
    """
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm()
    return render(request, 'vet_sprint/cita_form.html', {'form': form, 'accion': 'Crear'})

def cita_update(request, pk):
    """
    Permite actualizar una cita existente.
    """
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'vet_sprint/cita_form.html', {'form': form, 'accion': 'Actualizar'})

def cita_delete(request, pk):
    """
    Permite eliminar una cita.
    """
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('citas_list')
    return render(request, 'vet_sprint/cita_confirm_delete.html', {'cita': cita})