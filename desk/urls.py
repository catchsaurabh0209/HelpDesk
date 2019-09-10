from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/answer', views.answer_post, name='answer_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/question/', views.question_post, name='question_post'),
    path('login/', views.login, name='login'),
    path('user/', views.user, name='user'),
    


]
