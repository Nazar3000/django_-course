from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import StProfile


class StProfileInline(admin.StackedInline):
    model = StProfile

class UserAdmin(auth_admin.UserAdmin):
    # list_display = ['last_name', 'first_name']
    inlines = (StProfileInline,)

# class UsersFormAdmin(ModelForm):
#     pass

# class UsersAdmin1(admin.ModelAdmin):
    # list_display = ['last_name', 'first_name']
    # form = UsersFormAdmin
# replace existing User admin form

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(StProfile, UsersAdmin1)