from django.conf.urls import path
from polls.views import dashboard


urlpatterns = [
    path(r"^dashboard/",dashboard, name='dashboard'),
]