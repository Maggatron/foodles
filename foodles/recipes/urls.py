from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'foodles.recipes.views.home', name='home')
)
