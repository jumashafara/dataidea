from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='browse', view=views.browse, name='browse'),
    path(route='course-details/<int:id>', view=views.course_details, name='course_details'),

]