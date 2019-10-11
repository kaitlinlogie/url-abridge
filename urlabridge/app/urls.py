from django.urls import path

from . import views

urlpatterns = [
    path('<str:path>/', views.page_redirect, name='page_redirect')
]