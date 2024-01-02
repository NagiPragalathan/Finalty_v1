from django.shortcuts import render
from base.models import Contact_us
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,"index.html")

def list_out(request):
    contact_data = Contact_us.objects.all()
    return render(request, "list_out.html", {'contact_data': contact_data})

def underdev(request):
    return render(request, "underdev.html")

def contact_form(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mail_address = request.POST.get('mail')
        message = request.POST.get('message')
        print(fname,lname)
        # Assuming YourModelName is the name of your model
        Contact_us.objects.create(name=str(fname+" "+lname), mail_address=mail_address, message=message)
        return render(request, 'index.html')

    return render(request, 'index.html')

# for SEO...

def robots_txt(request):
    content = "User-agent: *\nDisallow: /private/\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")