# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Fieldset
from django.views.generic.edit import FormView
from django.utils.translation import ugettext as _

class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('profile', kwargs={'pk':kwargs['instance']})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'

        self.helper.add_input(Submit('add_button', _(u'Save'), css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', _(u'Cancel'), css_class="btn-link"))



class UserProfileView(FormView):
    template_name = 'registration/crispy_profile.html'
    form_class = UserProfileForm


    def get_success_url(self):
        return u'%s?status_message=Изменение успешно сохранены!' \
               % reverse('profile')


    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование профиля отменено!'
                                        % reverse('profile'))
        else:
            return super(UserProfileView, self).post(request, *args, **kwargs)