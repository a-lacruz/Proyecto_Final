from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from mvlcblog.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from mvlcblog.forms import UsuarioForm

def inicio(request):
    return render(request,"mvlcblog/inicio.html")

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
     model = Post
     success_url = reverse_lazy("mvlcblog-listar")
     fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("mvlcblog-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("mvlcblog-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('mvlcblog-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('mvlcblog-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mvlcblog-inicio')