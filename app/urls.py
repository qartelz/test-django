from django.urls import path
from .views import test  # relative import

urlpatterns = [
    path("", test, name="test"),
]
