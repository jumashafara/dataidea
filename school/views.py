from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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

# @login_required(login_url='accounts:signin')
def course_details(request, id):
    course = Course.objects.get(id=id)
    videos = course.videos.all()
    paginator = Paginator(videos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'course': course,
               'videos': page_obj}
    template_name = 'school/course_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)
