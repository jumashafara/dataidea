# Create a custom template filter in your Django app
# myapp/templatetags/myapp_extras.py

from django import template
from school.models import Choice  # Replace 'myapp' with the actual name of your app

register = template.Library()

@register.filter(name='choice_text')
def choice_text(choice_id, question_id):
    try:
        choice = Choice.objects.get(id=choice_id, question__id=question_id)
        return choice.text
    except Choice.DoesNotExist:
        return "N/A"  # Handle the case where the choice doesn't exist

# In your template, load the custom filter at the top of the file

