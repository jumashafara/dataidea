from .models import Note
from .models import Video
from .models import Course
from django.shortcuts import render
from django.shortcuts import redirect
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

    # pagination
    paginator = Paginator(videos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'course': course,
               'videos': page_obj,
               'user': request.user}
    template_name = 'school/course_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def comment(request, id):
    try:
        video = Video.objects.get(id=id)
        comment = request.POST['comment']
        user = request.user
        if user.is_anonymous:
            video.comments.create(comment=comment)
            message = """
                    Thanks for your comment! Please sign in to enjoy the full benefits of our services. 
                    Your comment has been saved and will be visible to other users after you refresh the page 😊.
                    """
            context = {'message': message, 'state': 'success'}
            template_name = 'components/message.html'
            return render(request=request, template_name=template_name, context=context)
        else:
            video.comments.create(comment=comment, user=user)
            return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        message = """
                    Sorry, something went wrong while saving your comment. 
                    Please try again later.
                    """
        context = {'message': message, 'state': 'warning'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)


# Notes Section 
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get(key='title')
        detail = request.POST.get(key='detail')
        note = Note(title=title, detail=detail, user=request.user)
        note.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        user_notes = Note.objects.filter(user = request.user)
        template_name = 'school/notes.html'
        context = {'notes': user_notes}
        return render(request=request, template_name=template_name, context=context)

def one_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get(key='title')
        detail = request.POST.get(key='detail')
        note = Note(title=title, detail=detail, user=request.user)
        note.save()
        return redirect(request.META.get('HTTP_REFERER'))
    elif request.method == 'DELETE':
        note.delete()
    else:
        template_name = 'school/note_detail.htmls'
        context = {'note': note}
        return render(request=request, template_name=template_name, context=context)








# http://127.0.0.1:8000/schoolcourse-details/3?page=2