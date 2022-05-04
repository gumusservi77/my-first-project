from django.urls import path
from polls.views import dashboard


urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]