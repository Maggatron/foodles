from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'foodles.recipes.views.home', name='home'),
    url(r'^edit(?:/(?P<id>[0-9]+)?$)?', 'foodles.recipes.views.edit_recipe', name='edit_recipe'),
)
