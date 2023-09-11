from .models import Price
from .models import Service
from .models import Feature
from .models import Contact
from .models import Feedback
from .models import Portfolio
from .models import CompanyInfo
from .models import Testimonial
from .models import TermOfService
from .models import FrequentlyAskedQuestion
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    prices = Price.objects.all()
    services = Service.objects.all()
    contacts = Contact.objects.all()
    features = Feature.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="DataIdea")
    
    context = {
        'faqs': faqs,
        'prices':prices,
        'services': services,
        'contacts': contacts,
        'features': features,
        'companyinfo': companyinfo,
        'portfolios': portfolios,
        'testimonials': testimonials,
    }
    
    template_name = 'index/home.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def portfolio_details(request, id):
    portfolio = Portfolio.objects.get(id=id)
    context = {'portfolio':portfolio}
    template_name = 'index/portfolio_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def back(request):
    return redirect(request.META.get('HTTP_REFERER'))

def feedback(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        feedback = Feedback(name=name, email=email, 
                            subject=subject, message=message)
        feedback.save()
    
        context = {'state': 'success', 'message': f'Thank you for contacting us {name}. We will get in touch as soon as possible.'}
    except Exception as e:
        context = {'state': 'warning', 'message': f'Something went wrong. Please try again later.'}

    template_name='components/message.html'
    return render(request=request, template_name=template_name, context=context)

def termsOfService(request):
    terms_of_service = TermOfService.objects.all()
    context = {'terms_of_service':terms_of_service}
    
    template_name='index/terms_of_service.html'
    return render(request=request, template_name=template_name, context=context)