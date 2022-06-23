from django.shortcuts import redirect, render

# Create your views here.
def service(request):
    context={'service': 'active' }
    return render(request,"serv/service.html",context)
