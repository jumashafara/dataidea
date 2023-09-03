from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='', view=views.browse, name='browse'),
    path(route='add_note/', view=views.add_note, name='add_note'),
    path(route='one_note/<int:id>', view=views.one_note, name='one_note'),
    path(route='comment/<int:id>', view=views.comment, name='comment'),
    path(route='course-details/<int:id>', view=views.course_details, name='course_details'),

]