from django.contrib import admin
from models import Imagen, Basurero, GPS, Reporte
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'Basureros Satelites'

admin.site.unregister(Group)

#admin.site.register(Imagen)
#admin.site.register(Basurero)
#admin.site.register(GPS)
#admin.site.register(Reporte)
