from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('update/<int:tid>', views.update, name = 'update'),
    path('delete/<int:tid>', views.delete, name = 'delete'),
    path('history', views.history, name = 'history'),
    path('restore<int:tid>', views.restore, name = 'restore'),

    path('create_cat', views.create_cat, name = 'create_cat'),
    path('read_cat', views.read_cat, name = 'read_cat'),
    path('update_cat/<int:tid>', views.update_cat, name = 'update_cat'),
    path('delete_cat/<int:tid>', views.delete_cat, name = 'delete_cat'),
    path('cat_history', views.cat_history, name = 'cat_history'),
    path('cat_restore<int:cid>', views.cat_restore, name = 'cat_restore'),
]