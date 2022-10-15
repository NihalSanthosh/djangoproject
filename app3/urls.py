from django.urls import path
from . import views 
app_name='app3'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('remove_user/<int:id>',views.remove_user,name='remove_user'),
    path('password_change/<int:id>',views.password_change,name='password_change'),
    path('logout',views.logout,name='logout'),
    path('view_users/',views.view_users,name='view_users'),
    path('gallery/',views.gallery,name='gallery'),
]
