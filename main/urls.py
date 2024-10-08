from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_login, name="user_login"),
    path("login/", views.user_login, name="logout"),
    path("register/", views.user_register, name="user_register"),
    path('quiz/', views.quiz, name='quiz'),
    path('score_card/', views.score_card_view, name='score_card'),
    path('add_question/', views.add_questions, name='add_question'),
]