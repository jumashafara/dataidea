from django.shortcuts import render
from .models import Course

# Create your views here.
def browse(request):
    courses = Course.objects.all()
    course_level_key_map = {'reception-1': 'Introduction'}
    context = {'courses': courses,
               'course_level_key_map': course_level_key_map}
    template_name = 'school/browse.html'
    return render(request=request, 
                  template_name=template_name,
                   context=context )
