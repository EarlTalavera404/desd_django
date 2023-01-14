from django.urls import path
from desd_assignment import views
from desd_assignment.models import ClubRep

home_list_view = views.HomeListView.as_view(
    context_object_name="club_rep_list",
    template_name="desd_assignment/home.html",
)


film_as_view = views.FilmListView.as_view(
    context_object_name="film_list",
    template_name="desd_assignment/film.html",
)

urlpatterns = [
    # Paths
    path("", home_list_view, name="home"),
    path("register/", views.ClubRepresentative.register, name="register"),
    path("film/", film_as_view, name="film"),
    path('update/<int:id>', views.ClubRepresentative.update, name='update'),
    path('delete/<int:id>', views.ClubRepresentative.delete, name='delete'),

]