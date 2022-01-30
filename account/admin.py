from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'category', 'is_active', 'is_admin')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ('email', 'username', 'category', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'category',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'category', 'password1', 'password2', 'is_staff', 'is_active',),
        }),
    )

admin.site.register(Account, AccountAdmin)