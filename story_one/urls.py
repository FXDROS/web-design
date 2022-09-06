from django.urls import path
from . import views

app_name = 'story_one'
urlpatterns = [
    path('', views.home_view, name="profile"),
    path('profile/', views.profile, name="profile"),
    path('gallery/', views.gallery, name="gallery"),
    path('schedule/', views.schedule, name="schedule"),
    path('schedule/<int:id_>/', views.delete, name="delete"),
    path('schedule/<int:id_>/detail', views.detail, name='detail'),
    path('events/', views.events, name="events"),
    path('events/apply/<int:id_>', views.apply, name="apply"),
    path('books/', views.books, name="books"),
    path('data/', views.books_data, name="data"),
] 