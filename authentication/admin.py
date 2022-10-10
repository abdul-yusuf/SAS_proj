from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin', 'is_landlord' )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('phone_no', 'nationality', 'state_of_origin')}),
        ('Permissions', {'fields': ('is_admin', 'is_landlord')}),
        ('Site Info', {'fields': ('specialization', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)