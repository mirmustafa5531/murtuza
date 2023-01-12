from django.shortcuts import render ,HttpResponseRedirect
from.forms import clubregistrations
from .models import user
from.forms import selectshowing
from.models import showing

# This function will add and retrieve data
def add_show(request):
    if request.method == 'POST':
        fm = clubregistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name = nm, email = em, password = pw)
            reg.save()                 
            fm = clubregistrations()
    else:       
        fm = clubregistrations()
    stud = user.objects.all()
    return render(request,'addandshow.html',{'form':fm,'stu':stud} )

#This function deletes data

def delete_data(request, id ):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()    
        return HttpResponseRedirect('/')

#This function will update the data

def update_data(request, id):
    if request.method == 'POST':
     pi = user.objects.get(pk = id)
     fm = clubregistrations(request.POST,instance=pi)
     if fm.is_valid():
        fm.save()
    else:
        pi = user.objects.get(pk = id)
        fm = clubregistrations(instance=pi)
    return render(request , r'crud\templates\updateclub.html',{'form':fm})


#This Function will add showings 
def add_showings(request):
    if request.method == 'POST':
        fm = selectshowing(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['filmtitle']
            em = fm.cleaned_data['agerating']
            pw = fm.cleaned_data['duration']
            reg = showing(filmtitle = nm, agerating = em, duration= pw)
            reg.save()                 
            fm = selectshowing()
    else:       
        fm = selectshowing()
    stud = showing.objects.all()
    return render(request,'addandviewshowing.html',{'form':fm,'stu':stud} )    