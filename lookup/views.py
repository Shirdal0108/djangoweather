from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=0&API_KEY=E96B24E8-D0BA-4500-BF20-C626D5817329")     
    
        try:
            api = json.loads(api_request.content)
        except api.DoesNotExist:
            raise Http404("Zipcode does not exist") 
            # api = "Error..."

        if api[0]['Category']['Name'] == "Good": 
            category_color = "good"   
        elif api[0]['Category']['Name'] == "Moderate": 
            category_color = "moderate" 
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Group": 
            category_color = "unhealthy for sensitive group" 
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy" 
        elif api[0]['Category']['Name'] == "Very Unhealthy": 
            category_color = "veryunhealthy" 
        elif api[0]['Category']['Name'] == "Hazardous": 
            category_color = "hazardous" 
           

        return render(request, 'home.html', {'api': api, 
           'category_color': category_color})
        

    else: 
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=0&API_KEY=E96B24E8-D0BA-4500-BF20-C626D5817329")

        try:
            api = json.loads(api_request.content)
        except api.DoesNotExist:
            raise Http404("Zipcode does not exist")    
        

        if api[0]['Category']['Name'] == "Good": 
            category_color = "good"   
        elif api[0]['Category']['Name'] == "Moderate": 
            category_color = "moderate" 
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Group": 
            category_color = "unhealthy for sensitive group" 
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy" 
        elif api[0]['Category']['Name'] == "Very Unhealthy": 
            category_color = "veryunhealthy" 
        elif api[0]['Category']['Name'] == "Hazardous": 
            category_color = "hazardous" 
    
        return render(request, 'home.html', {'api': api, 
          'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})    