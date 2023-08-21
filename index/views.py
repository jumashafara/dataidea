from .models import Price
from .models import Service
from .models import Feature
from .models import Contact
from .models import Feedback
from .models import Portfolio
from .models import Statistics
from .models import Testimonial
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
    statistics = Statistics.objects.get(
        name="Company statistics")
    
    context = {
        'faqs': faqs,
        'prices':prices,
        'services': services,
        'contacts': contacts,
        'features': features,
        'statistics': statistics,
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

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    print (name, email, subject, message)
    feedback = Feedback(name=name, email=email, 
                        subject=subject, message=message)
    feedback.save()

    return redirect('index:home')
