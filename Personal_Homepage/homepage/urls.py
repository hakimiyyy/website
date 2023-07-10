from django.urls import path
from .import views

urlpatterns=[
    
        path('',views.homepage, name ="lostandfound"),
        path('log_in',views.log_in, name ="log_in"),
        path('reporteditems',views.reporteditems, name ="reporteditems"),
        path('signup',views.signup, name ="signup"),
        path('lostitem',views.lostitem, name ="lostitem"),
        path('profile',views.profile, name ="profile"),
        path('delete/<str:username>', views.delete, name="delete"),
        path('inputitem',views.inputitem, name ="inputitem"),
        
]