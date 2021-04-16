# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from abc import abstractmethod, ABCMeta

class LoginRequiredClass(FormView):
    ''' Абстарктынй класс для класов вюх который вешает на метод класа вюхи
    dispatch проверку авторизации, унаследуй клас вюхи от этого класса и будет тебе счастье'''

    # C ABCMeta выглядит красиво но работает и без него
    __metaclass__ = ABCMeta

    # @abstractmethod
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredClass, self).dispatch(*args, **kwargs)


class PremissionRequiredClass(FormView):
    ''' Абстарктынй класс для класов вюх который вешает на метод класа вюхи
        dispatch проверку прав доступа авторизвоаного, унаследуй клас вюхи от этого класса и будет тебесчастье'''
    __metaclass__ = ABCMeta

    # @abstractmethod
    @method_decorator(permission_required('auth.add_user'))
    def dispatch(self, *args, **kwargs):
        return super(PremissionRequiredClass, self).dispatch(*args, **kwargs)