from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    b=showvideo.objects.all()
    context={'b':b}
    return render(request,'website/index.html',context)

def register(request):    
    return render(request,"website/register.html")

def loginpage(request):
        return render(request,"website/loginpage.html")

@csrf_exempt  
def log(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login/')
    else:
        form=loginform()
    return render(request,'registration/sign.html',{'form':form})


def logout_view(request):
    logout(request)
    print('ln 36 logout success')
    messages.success(request, 'logout success')
    return redirect('login')

def about(request):
        return render(request,"website/about.html")

def contact(request):
    return render(request,"website/contact.html")

def faq(request):
    return render(request,"website/faq.html")

def privacy(request):
    return render(request,"website/privacy.html")

def disclaimer(request):
    return render(request,"website/disclaimer.html")


def membership(request):
    return render(request,"website/membership.html")

def happystories(request):
    return render(request,"website/happystories.html")
    
def happystory(request):
    st=story.objects.all()
    context={'st':st}
    return render(request,'website/happystories.html',context)
    
def stories(request,id):
    st=story.objects.get(id=id)
    context={'st':st}
    return render(request,'website/storydetail.html',context)

def blogss(request):
    bl=blogs.objects.all()
    context={'bl':bl}
    return render(request,'website/blogs.html',context)
    
def blogdetail(request,id):
    bl=blogs.objects.get(id=id)
    context={'bl':bl}
    return render(request,'website/blogss.html',context)
    
def searchdetail(request):
   return render(request,"website/searchdetail.html")

@csrf_exempt   
def apply(request):
    if request.method=="POST":
        form=contacts(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    return render(request,'website/contact.html')
 
@csrf_exempt  
def insertregister(request):
    if request.method=="POST":
        form=searchsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/membership/')
    return render(request,'website/register.html')
 
def g(request):
    a=Searchs.objects.all()
    context={'a':a}
    return render(request,'website/searchs.html',context)
    

def serchdetail(request,id):
    sh=serch.objects.get(id=id)
    context={'sh':sh}
    return render(request,'website/searchdetail.html',context)
       

def search(request):
    return render(request,"website/search.html")
      
def filter_searched(request):    
    gender=request.GET['Gender']
    print('ln 100 gender ', gender)
    ms=request.GET['Maritial_status']    
    print('ln 102 Marital_status ', ms)
    agefrom=request.GET['age']
    print('ln 104 agefrom ', agefrom)
    ageto=request.GET['age1']
    print('ln 106 ageto ', ageto)
    religion=request.GET['religion']
    print('ln 108 religion ', religion)
    education=request.GET['education']
    print('ln 110 education ', education)
    occupation=request.GET['occupation']
    print('ln 112 occupation ', occupation)
    approval=request.GET['approval']
    print('ln 114 approval ', approval)
    data=Searchs.objects.filter(
        Gender=gender, 
        Maritial_status=ms,
        religion=religion, 
        education=education, 
        occupation=occupation, 
        age__range=[agefrom, ageto], 
        #approval=approval,
        )
    print('ln 144 data ', data)
    # user_id = data.user_id
    # print('ln 145 data.user_id ', user_id)
    context={'data':data}
    return render(request,'website/searched_profile.html',context)


@login_required
def view_searchs(request, searchs_id):
    searchs = get_object_or_404(Searchs, id=searchs_id)
    viewed_searchs, created = ViewedSearchs.objects.get_or_create(user=request.user, searchs=searchs)
    return render(request, 'website/view_searchs.html', {'searchs': searchs, 'viewed_searchs': viewed_searchs})

@login_required
def shortlist_searchs(request, searchs_id):
    searchs = get_object_or_404(Searchs, id=searchs_id)
    viewed_searchs, created = ViewedSearchs.objects.get_or_create(user=request.user, searchs=searchs)
    viewed_searchs.shortlisted = True
    viewed_searchs.save()

    return redirect('shortlisted')

@login_required
def shortlisted(request):
    shortlisted = ViewedSearchs.objects.filter(user=request.user, shortlisted=True)
    return render(request, 'website/shortlisted.html', {'shortlisted': shortlisted})


'''
@csrf_exempt  
def slists(request):
    if request.method=="POST":
        # user_id = user_id
        uid=request.POST['user']
        user_id = request.POST['slist']
        request.session['user_id'] = user_id
        print('ln 152 uid ', uid)        
        print('ln 155 user_id ', user_id)
        form=sform(request.POST)
        if form.is_valid():
            form.save()
            # print('ln 158 form ', form)
            return redirect('short', id=uid)
    return render(request,'website/searchbride.html')
'''
def short(request,id):
    user_id = request.session.get('user_id')
    # data=searchs.objects.get(user_id=user_id,slist='sort',)
    data=Searchs.objects.get(user_id=user_id)    
    print('ln 160 data ', data)
   
    context={'data':data}
    return render(request,'website/short.html',context)