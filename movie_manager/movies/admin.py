from django.contrib import admin
from . models import MovieInfo,Directors,CensorInfo,Actors
# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(Directors)
admin.site.register(CensorInfo)
admin.site.register(Actors)