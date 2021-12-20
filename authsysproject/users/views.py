from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ContactoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def home(request):
    form = CasoForm()
    if request.method == "POST":
        form = CasoForm(data=request.POST)
    else:
        return render(request, "users/home.html", {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hola {username}, Tu cuenta ha sido creada exitosamente"
            )
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required()
def profile(request):
    return render(request, "users/profile.html")


def mostrar_casos(request):
    casos = Caso.objects.all()
    return render(request, 'users/mostrar_casos.html', {'data': casos})


def registro_casos(request):
    if request.method == 'POST':
        form = CasoForm(data=request.POST)
        form.save(commit=True)
        return redirect('/')
    else:
        form = CasoForm()
        return render(request, 'users/registro.html', {'form': form})


def editar_casos(request, id):
    caso = Caso.objects.get(pk=id)
    form = CasoForm(instance=caso)
    if request.method == 'POST':
        form = CasoForm(data=request.POST, instance=caso)
        form.save()
        return redirect('/')
    else:
        return render(request, 'users/editar_caso.html', {'form': form})


def eliminar_casos(request, id):
    caso = Caso.objects.get(pk=id)
    caso.delete()
    return redirect('/')


def quehacemos(request):
    return render(request, "users/quehacemos.html")


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CONTACTO GUARDADO"
        else:
            data["form"] = formulario

    return render(request, "users/contacto.html", data)
