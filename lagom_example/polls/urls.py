from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('extra', views.CBVexample.as_view(), name='extra'),
    path('extra/<int:favourite_number>', views.CBVexampleWithPathParams.as_view(), name='extra_with_number'),
]
