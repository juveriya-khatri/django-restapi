from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role


#fields = list(UserAdmin.fieldsets)
#fields[0] = (None, {'fields': ('username', 'password', 'contact_number', 'role')})
#UserAdmin.fieldsets = tuple(fields)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('role', 'contact_number')}),

admin.site.register(Role)

admin.site.register(User, UserAdmin)
