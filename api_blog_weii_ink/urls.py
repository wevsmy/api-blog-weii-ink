from django.urls import path, include
from django.conf.urls import url

from django.contrib import admin

admin.autodiscover()

import hello.views
from .views import homePage

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    url(r'^$', homePage.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),

    # path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
]
