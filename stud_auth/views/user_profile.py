from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from ..models import StudentProfile
from  ..admin import UserAdmin, StudentProfileInline
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, MultiField, Div, HTML, Field, ButtonHolder, Button
from django.forms import ModelForm, ValidationError
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, FormView
from django.utils.translation import ugettext as _


class UserProfileView(TemplateView):
    template_name ='registration/profile_v2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.get(pk=kwargs['pk'])
        # queryset2 = StProfile.objects.all()
        # queryset = [User.objects.filter(pk=kwargs['pk'])]
        user1 = []
        # for data in queryset2:
        #     user1.append({'queryset2': data})
        user = queryset


        # for user in queryset:
        if user:
            user1.append({
            'fulname':'%s %s'%(user.last_name, user.first_name),
            'username':user.username,
            'id': user.id,
            'email': user.email,
            'date_joined':user.date_joined,
            # 'queryset2': queryset2,
            })
        # context['user1']= queryset
        context ['user1'] = user
        return context




class UserUpdateForm(ModelForm):

    class Meta:

        model = User
        fields=('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)


        # set form tag attributes
        self.helper.form_action = reverse('user_update', kwargs={'pk':kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'


        # set field propertyes
        self.helper.help_tex_iline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('add_button', _('Save'), css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', _('Cancel'), css_class="btn-link"))



class UserUpdateView(UpdateView):
    template_name = 'crispy_profile.html'
    form_class = UserUpdateForm
    model = User

    def get_success_url(self, **kwargs):
        return '%s?status_message=Профиль успешно отредактирован!' \
               % reverse('profile2',
                         # получаем id юзера и вставляем его в адрес
                         kwargs={'pk': self.object.pk})