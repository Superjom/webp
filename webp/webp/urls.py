from django.conf.urls import patterns, include, url


from webp.views import index, header, footer, left, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^header$', header),
    url(r'^footer$', footer),
    url(r'^left$', left),
    url(r'^login$', login),

    url(r'users/', include('webp.users.urls')),

)
