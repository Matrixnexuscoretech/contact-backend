from django.urls import path
from .views import contact_form, home

urlpatterns = [
    path('', home, name='home'),  # handles / and /contact/
    path('submit/', contact_form, name='contact_form'),
]
