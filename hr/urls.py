from django.urls import path
from hr import views

urlpatterns = [
    path('hrdash/', views.hrHome, name='hrdash'),
    path('candidatedetails/<int:id>/', views.hrCandidateDetails, name='candidatedetails'),
    path('postjob/', views.postJobs, name='postjob'),
    path('acceptapplication/', views.acceptApplication, name='acceptapplication'),
    path('rejectapplication/', views.rejectApplication, name='rejectapplication'),  # New URL
    path('login/hrdash/', views.hrHome, name='hrdash'),
]
