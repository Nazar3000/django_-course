# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django import forms
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Отправить'))

    from_email = forms.EmailField(
        label=u"Ваш Емейл Адрес")

    subject = forms.CharField(
        label=u"Оглавдение письма",
        max_length=128)

    message = forms.CharField(
        label=u"Текст сообщения",
        max_length=2560,
        widget=forms.Textarea)

    def send_email(self):
        pass

class Test_form(FormView):
    template_name = 'contact_admin/test_form.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        """This
        method is called
        for valid data"""
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['form_email']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])
        return super(Test_form, self).form_valid(form)

