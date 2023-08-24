from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='browse', view=views.browse, name='browse')
]