from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


import re
from django.utils.timezone import datetime

# Add these to existing imports at the top of the file:
from django.shortcuts import redirect
from desd_assignment.forms import RegisterClubRepForm,UpdateForm
from desd_assignment.models import *

from django.views.generic import ListView
from django.template import loader
from django.urls import reverse

class ClubRepresentative():


    #Register function for club rep:
    def register(request):
        form = RegisterClubRepForm(request.POST or None) 

        if request.method == "POST":
            if form.is_valid():
                message = form.save(commit=False)
                message.save()
                return redirect("home")
        else:
            return render(request, "desd_assignment/register.html", {"form": form})


    def update(request, id):
        mymember = ClubRep.objects.get(id=id)
        form = UpdateForm(instance=mymember)
        if request.method == 'POST':
            form = UpdateForm(request.POST,instance=mymember)
            repNumber = request.POST['repNumber']
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            password = request.POST['password']
            dob = request.POST['dob']
            member = ClubRep.objects.get(id=id)

            member.repNumber = repNumber
            member.firstName = firstName
            member.lastName = lastName
            member.password = password
            member.dob = dob
            member.save()

            if form.is_valid():
                message = form.save(commit=False)
                message.save()
                return redirect("home")
        else:
            return render(request, "desd_assignment/update.html", {"form": form})
     


    # function to delete club representatives based in id
    def delete(request,id):
        member = ClubRep.objects.get(id=id)
        member.delete()
        return redirect("home")






class FilmListView(ListView):
    """Renders the films page"""
    model = Films





class HomeListView(ListView):
    """Renders the home page"""
    model = ClubRep
    accountObj= ClubRepresentative()

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


