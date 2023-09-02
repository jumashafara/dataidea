from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='', view=views.browse, name='browse'),
    path(route='comment/<int:id>', view=views.comment, name='comment'),
    path(route='course-details/<int:id>', view=views.course_details, name='course_details'),

]