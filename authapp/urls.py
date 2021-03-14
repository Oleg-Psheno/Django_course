from django.urls import path, re_path
from authapp.views import register,login, logout, profile, send_verify_mail

app_name='authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', send_verify_mail, name = 'verify')
]