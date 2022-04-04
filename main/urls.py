from django.urls import path

from . views import *

app_name = 'main'

urlpatterns = [
     path('', ShowMain.as_view(), name = 'home'),
    # path('', index, name = 'home'),
    path('category/<int:cat_id>', category, name = 'category'),
    path('post/<pk>/', ShowPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path("search/", search.as_view(), name='search'),


]


