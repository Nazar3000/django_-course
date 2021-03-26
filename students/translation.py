# -*- coding: utf-8 -*-
# Model Translation

from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.utils import fallbacks
from .models import Student
from django.utils.translation import ugettext_lazy as _


class StudentlTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name', 'notes',)   # Select here the fields you want to translate
translator.register(Student, StudentlTranslationOptions)

# You can add as many models as you want to translate here