from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    display = ('name', 'description', 'url')

# Register your models here.
admin.site.register(Person, PersonAdmin)