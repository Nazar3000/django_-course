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