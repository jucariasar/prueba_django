from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(solicitud):
	return HttpResponse("Hola mundo. esta es una prueba de una vista.")


