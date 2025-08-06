from django.views.generic import TemplateView


class ProductTemplateView(TemplateView):
    template_name = 'shop/shop.html'
