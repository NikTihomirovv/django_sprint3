from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]

# LiNKS FOR HTML
# href="{% url 'pages:about' %}"
# href="{% url 'pages:rules' %}"
