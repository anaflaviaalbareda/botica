
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class Carrito(models.Model):
    idcarrito = models.AutoField(db_column='idCarrito', primary_key=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total',max_digits=11, decimal_places=1, blank=True, null=True) # Field name made lowercase.
    cantidad_productos = models.IntegerField(db_column='Cantidad_productos', blank=True, null=True)  # Field name made lowercase.
    timestap = models.DateTimeField(db_column='Timestap', blank=True, null=True, default=datetime.now)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Carrito'


class CarritoHasProducto(models.Model):
    id_has = models.AutoField(primary_key=True)
    carrito_idcarrito = models.ForeignKey(Carrito, models.DO_NOTHING, db_column='Carrito_idCarrito')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad',max_digits=11, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal',max_digits=11, decimal_places=1, blank=True, null=True) # Field name made lowercase.
    presentacion = models.ForeignKey('Presentacion', models.DO_NOTHING, db_column='Presentacion')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Carrito_has_Producto'
        unique_together = (('id_has', 'carrito_idcarrito', 'presentacion', 'producto'),)


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'


class Compra(models.Model):
    idcompra = models.AutoField(db_column='idCompra', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio_delivery = models.DecimalField(db_column='Precio delivery',max_digits=11, decimal_places=1, blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_direccion = models.CharField(db_column='Tipo direccion', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True, default=datetime.today)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.
    comprado = models.TextField(db_column='Comprado', blank=True, null=True)  # Field name made lowercase.
    entregado = models.BooleanField(db_column='Entregado', default=False)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total',max_digits=11, decimal_places=1, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'Compra'
        unique_together = (('idcompra', 'cliente_idcliente'),)


class DeliveryTabla(models.Model):
    iddelivery = models.IntegerField(db_column='idDelivery', primary_key=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio = models.CharField(db_column='Precio', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delivery_tabla'


class Presentacion(models.Model):
    idpresentacion = models.AutoField(db_column='idPresentacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.DecimalField(max_digits=11, decimal_places=1, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presentacion'
        unique_together = (('idpresentacion', 'producto'),)


class Producto(models.Model):
    idproductos = models.AutoField(db_column='idProductos', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=400)  # Field name made lowercase.
    id_interno = models.IntegerField()
    last_update = models.DateTimeField(db_column='Last_update', blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(db_column='Stock', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
