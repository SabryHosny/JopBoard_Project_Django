from django.contrib import admin

# Register your models here.
from .models import Jop, Category, Jop_Applier
admin.site.register(Jop)
admin.site.register(Category)
admin.site.register(Jop_Applier)
