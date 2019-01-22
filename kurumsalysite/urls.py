from django.urls import path
from .views import index, about, services, process, faq, contact

urlpatterns = [
    path('', index, name="index"),
    path('hakkimizda/', about, name="about"),
    path('hizmetlerimiz/', services, name="services"),
    path('surec/', process, name="process"),
    path('sorular/', faq, name="faq"),
    path('iletisim/', contact, name="contact")
]