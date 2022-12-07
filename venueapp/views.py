from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import VenueList

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def VenueView(request):

    user_email = request.user.email
    all_venue_items = VenueList.objects.filter(user=user_email)
    return render(request, 'venulist.html',  {'all_items':all_venue_items})


@login_required(login_url='/login')
def addvenueView(request):
    # x = request.POST.get('todotext')

    user_email = request.user.email
    new_item = VenueList()
    new_item.user = user_email
    new_item.content = request.POST.get('content')
    new_item.priority = request.POST.get('priority')
    new_item.save()
    return HttpResponseRedirect('/venue/') 


@login_required(login_url='/login')
def deleteVenueView(request, i):
    y = VenueList.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/venue/') 