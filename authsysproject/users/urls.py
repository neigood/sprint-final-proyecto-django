from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("registro", views.mostrar_casos, name="mostrarcomentarios"),
    path("registrarcaso", views.registro_casos, name="registrarcomentario"),
    path("editar/<int:id>/", views.editar_casos),
    path("eliminar/<int:id>/", views.eliminar_casos),
    path("quehacemos", views.quehacemos, name="quehacemos"),
    path("contacto", views.contacto, name="contacto")

]
