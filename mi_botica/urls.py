from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('productos/',views.productos,name='productos'),
	path('productos_view/',views.productos_view,name='productos_view'),
	path('pre_confirmacion/',views.pre_confirmacion,name='pre_confirmacion'),
	path('confirmacion/',views.confirmacion,name='confirmacion'),
	path('nosotros/',views.nosotros,name='nosotros'),
	path('delivery/',views.delivery,name='delivery'),
	path('login/',views.login_view,name='login_view'),
	path('forgot/',views.forgot,name='forgot'),
	path('forgot2/',views.forgot2,name='forgot2'),
	path('add_user/',views.add_user,name='add_user'),
	path('user_added/',views.user_added,name='user_added'),
	path('log_out/',views.logoutView, name='logoutView'),
	path('change_pass/',views.change_pass,name='change_pass'),
	path('add_carrito/',views.add_carrito,name='add_carrito'),
	path('delete_carrito/',views.del_carrito,name='del_carrito')


]