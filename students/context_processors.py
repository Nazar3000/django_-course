from  .util import get_groups, get_lang_list

def groups_processor(request):
    return {'GROUPS': get_groups(request)}

def lang_processor(request):
    return {'LANGS': get_lang_list(request)}