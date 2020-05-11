from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.sel,name='check'),
    path('first/',views.first, name = 'first'),
    path('first/proc/',views.firstProc, name = 'firstProc'),
    path('first/proc/<int:year>/<int:term>',views.firstExact,name = 'firstExact'),
    path('second/',views.second, name = 'second'),
    path('second/proc/',views.secondProc, name = 'secondProc'),
    path('second/proc/<int:year>/<int:term>/<str:ders_kod>',views.secondExact,name = 'secondExact'),
    path('third/',views.third, name = 'third'),
    path('third/proc/',views.thirdProc, name = 'thirdProc'),
    path('third/proc/<int:year>/<int:term>/<str:stud_id>',views.thirdExact,name = 'thirdExact'),
    path('fifth/',views.fifth, name = 'fifth'),
    path('fifth/proc/',views.fifthProc, name = 'fifthProc'),
    path('fifth/proc/<int:year>/<int:term>/<str:stud_id>',views.fifthExact,name = 'fifthExact'),
    path('sixth/',views.sixth, name = 'sixth'),
    path('sixth/proc/',views.sixthProc, name = 'sixthProc'),
    path('sixth/proc/<int:year>/<int:term>/<str:emp_id>',views.sixthExact,name = 'sixthExact'),
    path('seventh/',views.seventh, name = 'seventh'),
    path('seventh/proc/',views.seventhProc, name = 'seventhProc'),
    path('seventh/proc/<int:year>/<int:term>/<str:emp_id>',views.seventhExact,name = 'seventhExact'),
    path('eighth/',views.eighth, name = 'eighth'),
    path('eighth/proc/',views.eighthProc, name = 'eighthProc'),
    path('eighth/proc/<int:year>/<int:term>/<str:stud_id>',views.eighthExact,name = 'eighthExact'),
    path('nineth/', views.nineth, name='nineth'),
    path('nineth/proc/', views.ninethProc, name='ninethProc'),
    path('nineth/proc/<int:year>/<int:term>/<str:stud_id>', views.ninethExact, name='ninethExact'),
    path('thirteenth/', views.thirteenth, name='thirteenth'),
    path('sorry', views.sorry, name='sorry'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)