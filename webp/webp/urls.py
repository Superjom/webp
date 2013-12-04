import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

from django.conf.urls import patterns, include, url


from webp.views import index, header, footer, left, login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'webp.views.index', name='home'),
    url(r'^header$', header),
    url(r'^footer$', footer),
    url(r'^left$', left),
    url(r'^login$', login),
    url(r'^logout$', logout),

    url(r'users/', include('webp.users.urls')),
    url(r'', include('webp.module.urls')),

)
