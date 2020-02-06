from django.urls import path

from . import views
from .dependency_config import container


urlpatterns = [
    path('', container.view(views.index), name='index'),
    path('extra', container.view(views.CBVexample), name='extra'),
    path('extra/<int:favourite_number>', container.view(views.CBVexampleWithPathParams), name='extra_with_number'),
]
