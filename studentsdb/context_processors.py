from .settings import PORTAL_URL
import logging
def students_proc(request):
    # logging.info(format("{'*'*10}students_proc(request), {request}"))
    return {'PORTAL_URL': PORTAL_URL}