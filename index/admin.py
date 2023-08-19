from .models import Price
from .models import Service
from .models import Feature
from .models import Contact
from .models import Portfolio
from .models import Testimonial
from django.contrib import admin
from .models import FrequentlyAskedQuestion

# Register your models here.
admin.site.register(model_or_iterable=
                    [Service, Feature, Testimonial, Portfolio, Price, FrequentlyAskedQuestion, Contact])


