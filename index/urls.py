from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='portfolio_details/<int:id>', view=views.portfolio_details, name='portfolio_details')
]