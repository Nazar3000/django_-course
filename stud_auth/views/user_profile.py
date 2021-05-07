from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from ..models import StudentProfile
from  ..admin import UserAdmin


class UserProfileView(TemplateView):
    template_name ='registration/profile_v2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.get(pk=kwargs['pk'])
        # queryset2 = StProfile.objects.all()
        # queryset = [User.objects.filter(pk=kwargs['pk'])]
        user1 = []
        # for data in queryset2:
        #     user1.append({'queryset2': data})
        user = queryset


        # for user in queryset:
        if user:
            user1.append({
            'fulname':'%s %s'%(user.last_name, user.first_name),
            'username':user.username,
            'id': user.id,
            'email': user.email,
            'date_joined':user.date_joined,
            # 'queryset2': queryset2,
            })
        # context['user1']= queryset
        context ['user1'] = user
        return context