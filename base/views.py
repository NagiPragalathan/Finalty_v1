from django.shortcuts import render, redirect
from base.models import Contact_us
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def Home(request):
    return render(request,"index.html")

def list_out(request):
    contact_data = Contact_us.objects.all()
    return render(request, "list_out.html", {'contact_data': contact_data})

def delete_contact(request):
    if request.method == 'GET':
        contact_id = request.GET.get('contact_id', '')

        # Perform your logic to delete the contact from the database
        try:
            contact_to_delete = Contact_us.objects.get(pk=contact_id)
            contact_to_delete.delete()
            return JsonResponse({'success': True, 'message': 'Contact deleted successfully'})
        except Contact_us.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Contact not found'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

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
        return redirect("home")

    return render(request, 'index.html')

# for SEO...

def robots_txt(request):
    content = "User-agent: *\nDisallow: /private/\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")