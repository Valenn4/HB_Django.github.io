from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuariosForm

# Create your views here.

def login(request):
    if request.method=='POST':
        try:
            detalleUsuario= Usuarios.objects.get(user=request.POST['usuario'], password=request.POST['password'])
            request.session['usuario'] = detalleUsuario.user
            return render(request, 'dashboard.html')
        except Usuarios.DoesNotExist as e:
            print("No existe el usuario")
    return render(request, 'login.html')

def registro(request):
    formulario = UsuariosForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('../')
    context = {
        'formulario':formulario
    }
    return render(request, 'registro.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def panelUsuarios(request):
    usuarios = Usuarios.objects.all()
    
    context  = {
        'usuarios': usuarios
    }
    return render(request, 'panelUsuarios.html', context)

def borrarUsuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect('../panelUsuarios/')