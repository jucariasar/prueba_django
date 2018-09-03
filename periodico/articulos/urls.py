from django.urls import path

from .import views

# Este es el URLconf para llamar la vista

urlpatterns = [
	path('', views.index, name='index')
]