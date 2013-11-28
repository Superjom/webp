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
    url(r'^nonmarked/nonmarkedtac$', 'webp.module.views.nonmarked.tac.index', name="tac_index"),
    url(r'^nonmarked/tac/list$', 'webp.module.views.nonmarked.tac.list', name="tac_list"),
    # create
    url(r'^nonmarked/tac/createinit$', 'webp.module.views.nonmarked.tac.createinit', name="tac_createinit"),

    url(r'^nonmarked/tac/create', 'webp.module.views.nonmarked.tac.create', name="tac_create"),
    # del
    url(r'^nonmarked/tac/del', 'webp.module.views.nonmarked.tac.delete', name="tac_del"),
    
    # update
    url(r'^nonmarked/tac/updateinit', 'webp.module.views.nonmarked.tac.updateinit', name="tac_updateinit"),

    url(r'^nonmarked/tac/update', 'webp.module.views.nonmarked.tac.update', name="tac_update"),

    # ------------------------------------ anchorstat ------------------------------------------------

    url(r'^nonmarked/anchorstat/list', 'webp.module.views.nonmarked.anchorstat.list', name="anchorstat_list"),

    url(r'^nonmarked/anchorstat/show', 'webp.module.views.nonmarked.anchorstat.show', name="anchorstat_show"),

    url(r'^nonmarked/anchorstat/createinit', 'webp.module.views.nonmarked.anchorstat.createinit', name="anchorstat_createinit"),

    url(r'^nonmarked/anchorstat/create', 'webp.module.views.nonmarked.anchorstat.create', name="anchorstat_create"),

    url(r'^nonmarked/anchorstat/delete', 'webp.module.views.nonmarked.anchorstat.delete', name="anchorstat_delete"),

    url(r'^nonmarked/anchorstat/createschedule', 'webp.module.views.nonmarked.anchorstat.create_schedule', name="anchorstat_create_schedule"),

    url(r'^nonmarked/anchorstat', 'webp.module.views.nonmarked.anchorstat.index', name="anchorstat_index"),

    # ------------------------------------ anchorstat ------------------------------------------------



)





if __name__ == "__main__":
    pass

