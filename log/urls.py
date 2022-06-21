from django.urls import URLPattern, path,include
from .import views
urlpatterns=[
    path('',views.Home , name='home'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
]