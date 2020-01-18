from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/favicon.ico')),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
