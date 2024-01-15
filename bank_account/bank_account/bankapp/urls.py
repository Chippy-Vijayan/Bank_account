from django.urls import path,include
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name= 'bankapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('addbranches/', views.addbranches,name='addbranches'),
    path('subscription/', views.subscription, name='subscription'),

    # path('signin/', views.signin, name='signin'),
    # path('register/',views.register,name='register'),
    # path('signout/', views.signout, name='signout'),

]