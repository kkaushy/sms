from django.contrib import admin
from api.models import User, SMS
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'mobile_no', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile_no')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(User, CustomUserAdmin)



class SMSAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever', 'text',)
    list_filter = ('sender', 'reciever',)
    search_fields = ('text',)
    ordering = ('createdAt',)
    model = SMS
admin.site.register(SMS, SMSAdmin)
