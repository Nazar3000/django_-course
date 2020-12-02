from .settings import PORTAL_URL
<<<<<<< HEAD

def students_proc(request):
=======
import logging
def students_proc(request):
    # logging.info(format("{'*'*10}students_proc(request), {request}"))
>>>>>>> e336e2e04061f1c7141d0980d2e41951f3af73af
    return {'PORTAL_URL': PORTAL_URL}