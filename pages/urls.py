from django.urls import path

from pages.views import home_view, contact_view

app_name = 'pages'

urlpatterns = [
    path('',home_view, name='home'),
    path('contact/',contact_view, name='contact'),
]