from functools import partial
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="bounty-index"),
    url(r'^submit/$', views.submit, name="bounty-submit"),
    url(r'^thanks/$', views.thanks, name="bounty-thanks"),
    url(r'^project-instructions/$',
        partial(views.page, slug='project-instructions'),
        name="bounty-project-instructions"),
]
