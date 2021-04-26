# -*- coding: utf-8 -*-
from django.forms import ModelForm
# from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Fieldset
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from registration.backends.simple.views import RegistrationView
from django.conf import settings
try:
    from django.utils.module_loading import import_string
except ImportError:
    from registration.utils import import_string

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super(LoginForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        self.helper.layout = Layout(Fieldset(
            _('Login'),
            'username',
            'password'
        ))

        # form buttons
        self.helper.add_input(Submit('send_button', _(u'Login')))
        # self.helper.add_input(Submit('cancel_button', u'Отмена'))





class LoginFormView(FormView):
    template_name = 'crispy_registration.html'
    # form_class = LoginForm
    form_class = LoginForm


    def get_success_url(self):
        return u'%s?status_message=Успешно залогались' \
               % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Передумал авторизоваться'
                                        % reverse('home'))
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_views.login(request, user)
                    return HttpResponseRedirect(u'%s?status_message=Авторизовался'
                                                % reverse('home'))
                else:
                    return HttpResponseRedirect(u'%s?status_message=a disabled account error message'
                                                % reverse('login'))
            else:
                return HttpResponseRedirect(u'%s?status_message=Такого пользователя не существует'
                                            % reverse('login'))







REGISTRATION_FORM_PATH = getattr(settings, 'REGISTRATION_FORM', 'registration.forms.RegistrationForm')
REGISTRATION_FORM = import_string( REGISTRATION_FORM_PATH )


class RegistrationForm(REGISTRATION_FORM):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        self.helper.layout = Layout(Fieldset(
            _('Registration'),
            'username',
            'email',
            'password1',
            'password2'
        ))

        # form buttons

        self.helper.add_input(Submit('send_button', _(u'Register')))

class RegistrationViewCustom(RegistrationView):
    template_name = 'crispy_registration.html'
    # form_class = LoginForm
    form_class = RegistrationForm
