from django.urls import path
#now import the views.py file into this code
from . import views
#import trial_project

urlpatterns=[
  #path('',views.index),
  #path('',views.home_view),
  path('',views.home_view1),
  #path('',views.home_view2),
  #path('show/',views.show_view),
	path('show/', views.show_view ),
  path('<id>', views.detail_view),
  path('<id>/update', views.update_view),
  path('<id>/delete', views.delete_view ),
]

