# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # ------------------------------------ tac ------------------------------------------------
    url(r'^nonmarked/nonmarkedtac$', 'webp.module.views.nonmarked.tac_index', name="tac_index"),
    url(r'^nonmarked/tac/list$', 'webp.module.views.nonmarked.tac_list', name="tac_list"),
    # create
    url(r'^nonmarked/tac/createinit$', 'webp.module.views.nonmarked.createinit', name="tac_createinit"),

    url(r'^nonmarked/tac/create', 'webp.module.views.nonmarked.create', name="tac_create"),
    # del
    url(r'^nonmarked/tac/del', 'webp.module.views.nonmarked.delete', name="tac_del"),
    
    # update
    url(r'^nonmarked/tac/updateinit', 'webp.module.views.nonmarked.updateinit', name="tac_updateinit"),

    url(r'^nonmarked/tac/update', 'webp.module.views.nonmarked.update', name="tac_update"),

    # ------------------------------------ tac ------------------------------------------------
    url(r'^nonmarked/anchorstat', 'webp.module.views.anchorstat.index', name="anchorstat_index"),

    url(r'^nonmarked/anchorstat/list', 'webp.module.views.anchorstat.list', name="anchorstat_list"),

    url(r'^nonmarked/anchorstat/show', 'webp.module.views.anchorstat.show', name="anchorstat_show"),

)





if __name__ == "__main__":
    pass

