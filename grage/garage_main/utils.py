from django.views.generic import ListView  # type: ignore

from .models import *

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Add Article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Contacts', 'url_name': 'contact'},
        # {'title': 'Register', 'url_name': 'register'},
        # {'title': 'Login', 'url_name': 'login'},
        # {'title': 'Logout', 'url_name': 'logout'},
        ]


class DataMixin(ListView):
    model = AutoModels
    template_name = 'garage_main/index.html'
    context_object_name = 'model'
    paginate_by = 3

    def get_user_data(self, *, object_list=None, title, **kwargs):
        context = super().get_context_data(**kwargs)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context['menu'] = user_menu

        context['title'] = title
        if self.kwargs:
            context['cat_select'] = self.kwargs['model_add_id_1']
        else:
            context['cat_select'] = 0
        return context
