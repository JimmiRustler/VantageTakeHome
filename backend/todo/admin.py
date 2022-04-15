from turtle import title
from django.contrib import admin
from .models import AdInfo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')

admin.site.register(AdInfo,TodoAdmin)
# Register your models here.
