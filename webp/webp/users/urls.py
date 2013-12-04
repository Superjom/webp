# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

from django.conf.urls import patterns, url
from views import login

urlpatterns = patterns('',
    url(r'^login$', login),
)





if __name__ == "__main__":
    pass

