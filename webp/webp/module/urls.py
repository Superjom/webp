# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^nonmarked/nonmarkedtac$', 'webp.module.views.nonmarked.tac_index', name="tac_index"),
    url(r'^nonmarked/tac/list$', 'webp.module.views.nonmarked.tac_list', name="tac_list"),
)





if __name__ == "__main__":
    pass

