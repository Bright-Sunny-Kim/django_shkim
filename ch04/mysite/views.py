from django.views.generic.base import TemplateView
# from django.apps import apps    #추가
from django.http import HttpResponse


#-- TemplateView
class HomeView(TemplateView):

    template_name='home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['app_list']=['polls','books'] # 이 라인 대신 아래 5라인 추가
        # dictVerbose={}
        # for app in apps.get_app_configs():
        #     if 'site-packages' not in app.path:
        #         dictVerbose[app.label]=app.verbose_name
        # context['verbose_dict']=dictVerbose

        return context

# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")