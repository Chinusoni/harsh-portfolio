from django.shortcuts import render
from .models import Experience # Import your model

def cv_home(request):
    # Grab all the experience entries from the database
    all_experiences = Experience.objects.all() 
    
    # Package them in a 'context' dictionary
    context = {
        'experiences': all_experiences
    }
    
    # Send the context to the template
    return render(request, 'resume/cv.html', context)