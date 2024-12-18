from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('homepage/', homepage, name='home'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('disclaimer/', disclaimer, name='disclaimer'),
    path('faq/', faq, name='faq'),
    # path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    
    path('happystories/', happystories, name='happystories'),
    path('happystory/', happystory, name='happystory'),
    path('stories/<int:id>', stories, name=' stories'),
    path('blogss/', blogss, name='blogss'),
    path('blogdetail/<int:id>', blogdetail, name='blogdetail'),

    path('search/', search, name='search'),
    path('serchdetail/', serchdetail, name='serchdetail'),
    path('searchdetail/', searchdetail, name='searchdetail'),

    path('g/', g, name='g'),
    
    path('apply', apply, name='apply'),
    path('filter_searched', filter_searched, name='filter_searched'),    
    # path('slists', slists, name='slists'),
    path('short/<int:id>', short, name='short'),
    
    path('view_searchs/<int:searchs_id>/', view_searchs, name='view_searchs'),
    path('shortlist_searchs/<int:searchs_id>/shortlist/', shortlist_searchs, name='shortlist_searchs'),
    path('shortlisted/', shortlisted, name='shortlisted'),
    
    path('membership/', membership, name='membership'),

    path('register/', register, name='register'),
    path('insertregister/', insertregister, name='insertregister'),

    
    path('login/', LoginView.as_view(), name='login'),    
    path('logout/', logout_view, name='logout'), 
    path('log/', log, name='log'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
