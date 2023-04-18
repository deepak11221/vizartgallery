from django.contrib import admin
from .models import profile

# Register your models here.

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    '''Admin View for profile'''

    list_display = ('name', 'email', 'phone', 'address', 'city', 'state', 'pincode', 'created_on', 'updated_on')