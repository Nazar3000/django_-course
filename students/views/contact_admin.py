# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(
    label=u"Ваш Емейл Адрес")

    subject = forms.CharField(
        label=u"Оглавдение листа",
        max_length=128)

    message = forms.CharField(
        label=u"Текст сообщения",
        max_length=2560,
        widget=forms.Textarea)

def contact_admin(request):
    return render(request, 'contact_admin/form.html', {})
