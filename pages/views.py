from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from pages.forms import ContactModelForm
from pages.models import StoreModel


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'

class ContactFormView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactModelForm
    success_url = reverse_lazy("pages:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your contact has been sent to admins ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please, correct your data ❌")
        # Agar form xatolarini ko‘rsatmoqchi bo‘lsang, qo‘shing:
        # for field, errors in form.errors.items():
        #     messages.error(self.request, f"{field}: {'; '.join(errors)}")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stores"] = StoreModel.objects.filter(picked=True)[:2]
        return context