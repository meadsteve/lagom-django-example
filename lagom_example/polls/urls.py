from django.urls import path

from . import views
from .dependency_config import container

urlpatterns = [
    path('', container.partial(views.index), name='index'),
]
