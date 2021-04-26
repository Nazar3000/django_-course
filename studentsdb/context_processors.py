from .settings import PORTAL_URL
from util import get_users

def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}

def users_proc(request):
    return {'USERS_LIST':get_users(request)}