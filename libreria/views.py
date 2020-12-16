from django.shortcuts import render
from .models import Autore_ArducaDiego, Libro_ArducaDiego
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class AutoreDetailCBV(DetailView):
    model = Autore_ArducaDiego
    template_name = "autore.html"


class LibroListCBV(ListView):
    model = Libro_ArducaDiego
    template_name = "lista_libri.html"

