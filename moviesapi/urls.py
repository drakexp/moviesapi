from django.conf.urls import url
from django.contrib import admin
from movies.views import MoviesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^movies/', MoviesView.as_view(), name='movies'),
    url(r'^movies/(?P<id>[\w\W]*)', MoviesView.as_view(), name='moviesget')
]
