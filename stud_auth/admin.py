from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import StudentProfile

# 8ий рядок: даний клас зв’яже модель StudentProfile
# із формою редагу- вання моделі User в адмінці; він унаслідується від StackedInline класу;
# StackedInline дозволить показати елементи інших моделей одразу після основних полів моделі User;
class StudentProfileInline(admin.StackedInline):
    model = StudentProfile

# 11ий: а це уже клас, який відповідатиме за форму редагування об’єкта User в адмінці;
# по-суті, ним ми хочемо перекрити уже існуючу форму User в адмінці;
# тому унаслідуємось від UserAdmin форми, що міститься в django.contrib.auth аплікації
# і далі всередині класу дописуємо те, що хочемо змінити;
class UserAdmin(auth_admin.UserAdmin):
    # list_display = ['last_name', 'first_name']
    inlines = (StudentProfileInline,)

# class UsersFormAdmin(ModelForm):
#     pass

# class UsersAdmin1(admin.ModelAdmin):
    # list_display = ['last_name', 'first_name']
    # form = UsersFormAdmin
# replace existing User admin form

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(StProfile, UsersAdmin1)