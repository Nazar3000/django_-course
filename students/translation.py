# -*- coding: utf-8 -*-
# Model Translation

from modeltranslation.translator import translator, TranslationOptions
from .models import Student


class StudentlTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name', 'birthday','notes','photo', 'ticket', 'student_group',)   # Select here the fields you want to translate
translator.register(Student, StudentlTranslationOptions)

# You can add as many models as you want to translate here