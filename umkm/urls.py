from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='umkm-list'), 
    path('<int:list_all_id>', views.umkm_views, name='list_all')
        ]
