from django.shortcuts import render

# Create your views here.
def browse(request):
    context = {}
    template_name = 'school/browse.html'
    return render(request=request, 
                  template_name=template_name,
                   context=context )
