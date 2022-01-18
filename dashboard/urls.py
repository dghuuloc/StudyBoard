from django.urls import path
from . import views 

# Create your paths here. 
urlpatterns = [ 
        path('', views.home, name='home'),
        path('notes/', views.notes, name='notes'),
        path('delete_notes/<str:pk>/', views.delete_notes, name='delete-note'),

        path('homework/', views.homework, name='homework'),
        path('update_homework/<str:pk>/', views.update_homework, name='update-homework'),
        path('delete_homework/<str:pk>/', views.delete_homework, name='delete-homework'),

        path('youtube/', views.youtube, name='youtube'),

        path('toto/', views.todo, name='todo'),
        path('update_toto/<str:pk>/', views.update_todo, name='update-todo'),
        path('delete_todo/<str:pk>/', views.delete_todo, name='delete-todo'),

        path('books/', views.books, name='books'),

        path('dictionary/', views.dictionary, name='dictionary'),

        path('wiki/', views.wiki, name='wiki'),

        path('conversion/', views.conversion, name='conversion'),
        ]
