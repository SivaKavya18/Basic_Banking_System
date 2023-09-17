from django.urls import path,include
from . import views
urlpatterns=[
 path('',views.home,name='home'),
 path('home',views.home,name='home'),
 path('all_customers/',views.all_customers),
 path('customer/<int:id>/',views.customer),
 path('transfer/<int:id1>/<int:id2>/',views.transfer),
 path('tran/<int:id1>/<int:id2>/',views.tran),
 path('main/',views.main),
 path('search/',views.search),
 path('transfer_history/',views.transfer_history),
 path('about_us/',views.about_us),
]
