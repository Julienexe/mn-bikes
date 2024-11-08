from django.contrib import admin

from riders.forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Rider, Lease,Testimonial

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Rider)
admin.site.register(Lease)
admin.site.register(Testimonial)
admin.site.site_header = "MN Transport Admin"
