from django.urls import path
from .views import home,registerPage,loginPage,logoutUser,categories,Health,Sports,Entertainment,General,Bussiness,Technology,Science,Search

urlpatterns = [
path('register/', registerPage, name="register"),
path('login/', loginPage, name="login"),  
path('logout/', logoutUser, name="logout"),
path('categories/',categories,name='categories'),
path('', home, name = "home"),
path('health/',Health,name='health'),
path('sports/',Sports,name='sports'),
path('entertainment/',Entertainment,name='entertainment'),
path('general/',General,name='general'),
path('bussiness/',Bussiness,name='bussiness'),
path('technology/',Technology,name='technology'),
path('science/',Science,name='science'),
path('search/',Search,name='search'),
]