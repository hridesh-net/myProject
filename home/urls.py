from django.urls import path
from home.views import hello_world, nav_bar, get_books, create_book, HomeView

urlpatterns = [
    path("", hello_world),
    path("nav/",nav_bar),
    path("book/<int:id>/", get_books),
    path("create/", create_book),
    path("Home_v/", HomeView.as_view())
]
