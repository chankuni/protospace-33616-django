from django.urls import path
from .views import signup, login, logout, UserDetail

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('users/<int:pk>/', UserDetail.as_view(), name='detail'),

]