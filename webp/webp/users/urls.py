# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

from django.conf.urls import patterns, url
from views import login

urlpatterns = patterns('',
    url(r'^login$', login),
)





if __name__ == "__main__":
    pass

