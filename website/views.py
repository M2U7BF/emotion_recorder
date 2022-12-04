from .const import common
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data() # 辞書型になっている
        ctxt = common.PARAMS
        return ctxt

# class AboutView(TemplateView):
#     template_name = "about.html"