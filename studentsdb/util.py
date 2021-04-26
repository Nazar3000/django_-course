from django.contrib.auth.models import User


def get_users(request):

    # cur_user = get_current_user(request)
    user_obj = User.objects.all()
    users = []

    for user in user_obj:
        users.append({
            'id':user.id,
            'username': user.username,
            # 'usermail':user.mobile_phone
        })
    return users
