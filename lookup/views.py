from django.shortcuts import render

def home(request):
    
    import json
    import requests

    if request.method == "POST":
        # zipcode = request.POST['zipcode']
        zipco = request.POST["abc"]
        # return render(request,'home.html',{'zipco': zipco })
    
    
        # api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=2193A50C-794E-49D8-AFD4-8353E4146A51")
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipco +"&distance=102&API_KEY=2193A50C-794E-49D8-AFD4-8353E4146A51")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = ("Error..")

        return render(request,'home.html',{'api': api})
    else:
        # api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=2193A50C-794E-49D8-AFD4-8353E4146A51")
        # try:
        #     api = json.loads(api_request.content)
        # except Exception as e:
        #     api = ("Error..")

        return render(request,'home.html',{})
    
        


def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})