# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def paginate(objects, size, request, context, var_name='object_list'):

    '''Paginate objects provided by view

     This function takes:
         *lisrt of elements;
         *number of objects per page;
         *request object to get urk parameters from;
         *var_name - variable name for list of objects.

     It returns updated context object.
     '''
    #apply pagination
    paginator = Paginator(objects, size)

    # try to get page number from request
    page = request.GET.get('page', '1')
    try:
        objects_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        objects_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g 9999),
        # deliver last page of results
        objects_list = paginator.page(paginator.num_pages)

    # set variables into context

    context[var_name] = objects_list
    context['is_paginated'] = objects_list.has_other_pages()
    context['page_obj'] = objects_list
    context['paginator'] = paginator

    return context

def get_groups(request):
    '''Returns list of existing groups'''
    # deferred import of Group model to avoid cycled imports
    from .models import Group

    # get currently selected group
    cur_group = get_current_group(request)
    group_obj = Group.objects.all().order_by('title')
    groups = []
    for group in group_obj:
        groups.append({

            'id': group.id,
            'title': group.title,
            'leader': group.leader and (u'%s %s' % (group.leader.first_name,
                                                    group.leader.last_name)) or None,
            'selected': cur_group and cur_group.id == group.id and True or False

        })
    return groups

def get_current_group(request):
    '''Returns currently selected group or None'''

    # we remember selected group in a cookie
    pk = request.COOKIES.get('current_group')

    if pk:
        from .models import Group
        try:
            group = Group.objects.get(pk=int(pk))
        except Group.DoesNotExist:
            return None
        else:
            return group
    else:
        return None

# Получаем список доступных языков из сетингза для контекстпроцессора
def get_lang_list(request):
    from studentsdb.settings import LANGUAGE_List
    curent_language = get_curent_language(request)
    languages = []
    for language in LANGUAGE_List:
        languages.append({
            'language':language,
            'title': language.title,
            'selected':curent_language and curent_language == language and True or False,

        }
        )
    return languages

# Возвращаем язык который записали в куки при выборе на фронте
def get_curent_language(request):
    lang = request.COOKIES.get('django_language')
    if lang:
        return lang
    else:
        return None