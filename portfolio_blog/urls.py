from django.urls import path
from portfolio_blog import views


urlpatterns = [
   path('', views.post_article, name="post_article"),
]
