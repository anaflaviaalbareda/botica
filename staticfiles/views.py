from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'mi_botica/index.html')

def productos(request):
	return render(request,'mi_botica/productos.html')

def productos_view(request):
	return render(request,'mi_botica/productos_view.html')

def pre_confirmacion(request):
	return render(request,'mi_botica/pre_confirmacion.html')

def confirmacion(request):
	return render(request,'mi_botica/confirmacion.html')

def nosotros(request):
	return render(request,'mi_botica/nosotros.html')

def delivery(request):
	return render(request,'mi_botica/delivery.html')

def login(request):
	return render(request,'mi_botica/login.html')

def add_user(request):
	return render(request,'mi_botica/add_user.html')

def user_added(request):
	return render(request,'mi_botica/user_added.html')