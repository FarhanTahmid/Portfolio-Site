from urllib.parse import urlparse
from django.urls import path,include
from .import views
app_name='portfolio_app'
urlpatterns = [
    path('',views.homepage,name='homepage'),
]
