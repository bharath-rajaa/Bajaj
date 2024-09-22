from django.urls import path
from bfhl_app.views import bfhl_post, bfhl_get

urlpatterns = [
    path('bfhl', bfhl_post, name='bfhl_post'),
    path('bfhl', bfhl_get, name='bfhl_get'),
]
from django.urls import path
from bfhl_app import views

urlpatterns = [
    path('', views.frontend_view, name='frontend_view'),
    path('bfhl', views.bfhl_post, name='bfhl_post'),  # POST request handler
    path('bfhl', views.bfhl_get, name='bfhl_get'),  # GET request handler
]
