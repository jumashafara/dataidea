from .models import Service
from .models import Feature
from .models import Contact
from .models import Portfolio
from .models import Testimonial
from django.shortcuts import render
from .models import FrequentlyAskedQuestion


# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()
    services = Service.objects.all()
    contacts = Contact.objects.all()
    testimonials = Testimonial.objects.all()
    features = Feature.objects.all()

    context = {
        'services': services,
        'contacts': contacts,
        'features': features,
        'portfolios': portfolios,
        'testimonials': testimonials,
    }
    
    template_name = 'index/home.html'
    return render(request=request, template_name=template_name, context=context)


def portfolio_details(request, id):
    portfolio = Portfolio.objects.get(id=id)
    context = {'portfolio':portfolio}
    template_name = 'index/portfolio_details.html'
    return render(request=request, template_name=template_name, context=context)