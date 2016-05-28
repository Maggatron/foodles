from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'foodles.recipes.views.home', name='home'),
    url(r'^add$', 'foodles.recipes.views.add_recipe', name='add_recipe'),
)
