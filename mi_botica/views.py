from django.shortcuts import render, redirect
from numpy import random
from .models import Producto, Presentacion, Compra, Cliente, Carrito, CarritoHasProducto

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from time import gmtime, strftime
import datetime
from datetime import timedelta

from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

import random

# Create your views here.
def index(request):
	return render(request,'mi_botica/index.html')

def productos(request):
	if request.GET:
		buscador=request.GET['buscador']
		buscador=buscador
		productos=Producto.objects.filter(descripcion__icontains=buscador)
	else:
		productos=Producto.objects.all().order_by('descripcion')[:15]
	
	dic={'productos':productos}


	return render(request,'mi_botica/productos.html',dic)

def productos_view(request):
	print('carrito',request.session.get('id_cart'))
	if request.GET:
		id_producto=request.GET['producto']
		producto=Producto.objects.get(idproductos=id_producto)
		presentaciones=Presentacion.objects.filter(producto=id_producto)
		dic={'producto':producto,'presentaciones':presentaciones}
	else:
		return redirect('../productos/')

	return render(request,'mi_botica/productos_view.html',dic)

def add_carrito(request):

	if request.user.is_authenticated:
		if request.session.get('id_cart', False):
			#get carrito
			id_cart=request.session['id_cart']
			carrito=Carrito.objects.get(idcarrito=id_cart)
			#get post
			producto=Producto.objects.get(idproductos=request.POST['producto'])
			presentacion=Presentacion.objects.get(idpresentacion=request.POST['presentacion'])
			print(presentacion)
			cantidad=request.POST['cantidad']
			subtotal=int(cantidad)*presentacion.precio
			test=CarritoHasProducto.objects.filter(carrito_idcarrito=carrito,presentacion=presentacion)
			print(test)
			if test:
				print("enter test producto")
				#Actualizar CarritoHasProducto
				test[0].cantidad+=int(cantidad)
				test[0].subtotal+=subtotal
				test[0].save()

				#Actualizar Carrito
				#request.session['cantidad']=request.session['cantidad']+1
				carrito.total=carrito.total+subtotal
				carrito.save()
				#print(producto,presentacion,cantidad)
				return redirect('../login')
			else:
				#Crear carrito has producto
				carrito_has_p=CarritoHasProducto(carrito_idcarrito=carrito,
					cantidad=cantidad,subtotal=subtotal,presentacion=presentacion,producto=producto)
				carrito_has_p.save()

				#Actualizar carrito
				request.session['cantidad']=request.session['cantidad']+1
				#print(request.session['cantidad'])
				carrito.cantidad_productos+=1
				carrito.total=carrito.total+subtotal
				carrito.save()
				#print(producto,presentacion,cantidad)

		else:
			#crear carrito
			carrito= Carrito()
			carrito.save()
			id_cart=carrito.idcarrito
			request.session['id_cart']=id_cart
			
			#print(request.session['cantidad'])
			producto=Producto.objects.get(idproductos=request.POST['producto'])
			presentacion=Presentacion.objects.get(idpresentacion=request.POST['presentacion'])
			cantidad=request.POST['cantidad']
			subtotal=int(cantidad)*presentacion.precio

			#crear carrito has producto

			carrito_has_p=CarritoHasProducto(carrito_idcarrito=carrito,
				cantidad=cantidad,subtotal=subtotal,presentacion=presentacion,producto=producto)
			carrito_has_p.save()

			#Actualizar carrito
			request.session['cantidad']=1
			#print(request.session['id_cart'])
			carrito.cantidad_productos=1
			carrito.total=subtotal
			carrito.save()
			#print(producto,presentacion,cantidad)

		return redirect('../productos')
	else:
		return redirect('../login')

def del_carrito(request):
	eliminar=CarritoHasProducto.objects.get(id_has=int(request.POST['eliminar']))
	subtotal=eliminar.subtotal
	carrito=Carrito.objects.get(idcarrito=eliminar.carrito_idcarrito.idcarrito)
	carrito.total=carrito.total-subtotal
	carrito.cantidad_productos-=1
	carrito.save()
	request.session['cantidad']=request.session['cantidad']-1
	eliminar.delete()
	return redirect('../login')

def pre_confirmacion(request):
	if request.user.is_authenticated:
		id_cart=request.session['id_cart']
		carrito=Carrito.objects.get(idcarrito=id_cart)
		productos_en_carrito=CarritoHasProducto.objects.filter(carrito_idcarrito=request.session['id_cart'])
		dic={'carrito':carrito,'productos':productos_en_carrito}
		return render(request,'mi_botica/pre_confirm.html',dic)
	else:
		return redirect('../login')

def confirmacion(request):
	if request.user.is_authenticated:
		direccion=request.POST['direccion']
		tipo_direccion=request.POST['tipo_direccion']
		estado=request.POST['estado']
		distrito=request.POST['distrito']
		username= request.user.username
		user=User.objects.get(username=username)
		cliente=Cliente.objects.get(user=user)
		id_cart=request.session['id_cart']
		carrito=Carrito.objects.get(idcarrito=id_cart)
		productos_en_carrito=CarritoHasProducto.objects.filter(carrito_idcarrito=request.session['id_cart'])
		Texto="Productos comprados: \n"
		for c in productos_en_carrito:
			cantidad= str(c.cantidad)
			subtotal= str(c.subtotal)
			presentacion= str(c.presentacion.nombre)
			producto= str(c.producto.descripcion)
			linea=producto+': '+cantidad+' '+presentacion+'- S./ '+subtotal+'\n'
			Texto=Texto+linea

		compra=Compra(direccion=direccion,precio_delivery=10,tipo_direccion=tipo_direccion,estado=estado,distrito=distrito,comprado=Texto,cliente_idcliente=cliente,total=carrito.total)
		compra.save()
		dic={'compra':compra,'cliente':cliente}

		#Email de delivery
		template = get_template('mi_botica/emai_compra.html')
		context = {'cliente': cliente, 'compra': compra}
		contenido = template.render(context)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [cliente.email,]
		asunto='Compra en Mi Botica Providencia'
		send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
		request.session.flush()
		
		return render(request,'mi_botica/confirm.html',dic)
	else:
		return redirect('../login')

	return render(request,'mi_botica/confirmacion.html')

def nosotros(request):
	return render(request,'mi_botica/nosotros.html')

def delivery(request):
	return render(request,'mi_botica/delivery.html')

def login_view(request):
	if request.POST:
		username = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			cliente=Cliente.objects.get(user=user)
			login(request, user)
			dic={'cliente':cliente, 'texto_grande': "Bienvenido",'texto_chico':'Revisa los detalles de tu cuenta a continuación'}
			#print('hola')
			if 'id_cart' in request.session:
				#print("paso")
				productos_en_carrito=CarritoHasProducto.objects.filter(carrito_idcarrito=request.session['id_cart'])
				dic['productos_en_carrito']=productos_en_carrito
				dic['carrito']=Carrito.objects.get(idcarrito=request.session['id_cart'])

			#print(request.session.get('id_cart'))

			return render(request,'mi_botica/login.html',dic)
		else:
			dic={'texto_grande': "Ingreso para clientes",'texto_chico':'Bienvenido a Botica Providencia Online, ingresa con tu email y contraseña','alerta':"El usuario o la constraseña no coinciden"}
			return render(request,'mi_botica/login.html',dic)
	else:
		if request.user.is_authenticated:
			user=request.user
			cliente=Cliente.objects.get(user=user)
			dic={'cliente':cliente, 'texto_grande': "Bienvenida Socia",'texto_chico':'Revisa los detalles de tu cuenta a continuación'}
			if 'id_cart' in request.session:
				productos_en_carrito=CarritoHasProducto.objects.filter(carrito_idcarrito=request.session['id_cart'])
				dic['productos_en_carrito']=productos_en_carrito
				dic['carrito']=Carrito.objects.get(idcarrito=request.session['id_cart'])

			#print(request.session.get('id_cart'))
		else:
			dic={'texto_grande': "Ingreso para Socias ADP",'texto_chico':'Bienvenida al portal de socias, ingresa con tus credenciales'}
		
		return render(request, 'mi_botica/login.html',dic)

def add_user(request):
	return render(request,'mi_botica/add_user.html')

def user_added(request):
	email=request.POST['email']
	exist= User.objects.filter(username=email).exists()

	if exist:
		dic={'titulo':'Usuario ya existe','alerta':'Ya existe una cuenta asociada a este email. Puede recuperar su contraseña en la seccion de Ingreso'}
		
		return render(request,'mi_botica/user_added.html',dic)
	
	else:
		
		nombre=request.POST['nombre']
		apellido=request.POST['apellido']
		telefono=request.POST['phone']
		contrasena=request.POST['password']
		email=request.POST['email']
		usuario=User.objects.create_user(username=email,password=contrasena,email=email)
		usuario.save()
		cliente=Cliente(user=usuario,email=email,nombre=nombre,apellido=apellido,contrasena=contrasena,telefono=telefono)
		cliente.save()
		dic={'titulo':'Usuario añadido con exito','alerta':'ya existe una cuenta asociada a este email. Puede recuperar su contraseña en la seccion de Ingreso'}
		
		return render(request,'mi_botica/user_added.html',dic)

def logoutView(request):
	logout(request)
	return redirect('/')

def forgot(request):
	return render(request,'mi_botica/forgot.html')

def forgot2(request):
	new_pass=random.randint(10000,99999)
	email=request.POST['email']
	exist= User.objects.filter(username=email).exists()
	if exist:
		u=User.objects.get(username=email)
		u.set_password(new_pass)
		u.save()
		cliente=Cliente.objects.get(user=u)
		template = get_template('mi_botica/email_forgot.html')
		context = {'cliente': cliente, 'new_pass': new_pass}
		contenido = template.render(context)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]
		asunto='Contraseña olvidadad Mi Botica Providencia'
		send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
		return redirect('../login')
	else:
		return render(request,'mi_botica/forgot2.html')

def change_pass(request):
	if request.POST:
		user=request.user
		new_pass=request.POST['password']
		user.set_password(new_pass)
		user.save()
		return redirect('../login')
	else:
		return render(request,'mi_botica/change_pass.html')





