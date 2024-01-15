from django.urls import path,include

from credential import views
from bank_account import settings
from django.conf.urls.static import static
app_name= 'credential'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    ]