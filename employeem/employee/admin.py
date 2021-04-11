from django.contrib import admin

# Register your models here.
from .models import Empid

# Register your models here.
@admin.register(Empid)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','post','bloodgroup')
