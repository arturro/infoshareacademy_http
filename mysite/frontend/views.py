from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'frontend/home_page.html'


class VueView(TemplateView):
    template_name = 'frontend/vue.html'
