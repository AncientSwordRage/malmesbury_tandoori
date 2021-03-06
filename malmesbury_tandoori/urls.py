from django.conf.urls import patterns, include, url
from django.contrib import admin
from tandoor.views import FoodCategoryListView, HomeView, AboutView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'malmesbury_tandoori.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/?', include(admin.site.urls)),
    url(r'^menu/?$', FoodCategoryListView.as_view(),name='menu'),
    url(r'^about/?$', AboutView.as_view(), name='about'),
    url(r'^.*',HomeView.as_view()),
)
