from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin', views.signin, name = 'signin'),
    path('profile', views.profile, name = 'profile'),
    path('update_det', views.update_det, name = 'update_det'),
    path('update_pw', views.update_pw, name = 'update_pw'),
    path('signout', views.signout, name = 'signout')
]