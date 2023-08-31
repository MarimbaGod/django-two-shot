from django.urls import path
from accounts.views import user_login

# create url path

urlpatterns = [
    path("login/", user_login, name="login"),
]
