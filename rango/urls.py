from django.urls import path
from rango import views

app_name='rango'

urlpatterns = [
    #path(string to match, what to call if string matches, (optional) name -> convenient for referencing the view)
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category')
]