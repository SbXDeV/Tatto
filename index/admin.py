from django.contrib import admin
from .models import WriteToMaster


# Register your models here.

@admin.register(WriteToMaster)
class AuthorAdmin(admin.ModelAdmin):
    pass
