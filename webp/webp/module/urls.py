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

    url(r'^nonmarked/anchorstat/list?.*', 'webp.module.views.nonmarked.anchorstat.list', name="anchorstat_list"),

    url(r'^nonmarked/anchorstat/show?.*', 'webp.module.views.nonmarked.anchorstat.show', name="anchorstat_show"),

    url(r'^nonmarked/anchorstat/createinit?.*', 'webp.module.views.nonmarked.anchorstat.createinit', name="anchorstat_createinit"),

    url(r'^nonmarked/anchorstat/delete?.*', 'webp.module.views.nonmarked.anchorstat.delete', name="anchorstat_delete"),

    url(r'^nonmarked/anchorstat/createschedule?.*', 'webp.module.views.nonmarked.anchorstat.create_schedule', name="anchorstat_create_schedule"),

    url(r'^nonmarked/anchorstat/create?.*', 'webp.module.views.nonmarked.anchorstat.create', name="anchorstat_create"),

    url(r'^nonmarked/anchorstat?.*', 'webp.module.views.nonmarked.anchorstat.index', name="anchorstat_index"),

    # ------------------------------------ fieldstat ------------------------------------------------
    url(r'^nonmarked/fieldstat/list', 'webp.module.views.nonmarked.fieldstat.list', name="fieldstat_list"),

    url(r'^nonmarked/fieldstat/show', 'webp.module.views.nonmarked.fieldstat.show', name="fieldstat_show"),

    url(r'^nonmarked/fieldstat/createinit', 'webp.module.views.nonmarked.fieldstat.createinit', name="fieldstat_createinit"),

    url(r'^nonmarked/fieldstat/create', 'webp.module.views.nonmarked.fieldstat.create', name="fieldstat_create"),

    url(r'^nonmarked/fieldstat/delete', 'webp.module.views.nonmarked.fieldstat.delete', name="fieldstat_delete"),

    url(r'^nonmarked/fieldstat/createschedule', 'webp.module.views.nonmarked.fieldstat.create_schedule', name="fieldstat_create_schedule"),

    url(r'^nonmarked/fieldstat', 'webp.module.views.nonmarked.fieldstat.index', name="fieldstat_index"),

    # ------------------------------------ linkcount ------------------------------------------------
    url(r'^nonmarked/linkcount/list', 'webp.module.views.nonmarked.linkcount.list', name="linkcount_list"),

    url(r'^nonmarked/linkcount/show', 'webp.module.views.nonmarked.linkcount.show', name="linkcount_show"),

    url(r'^nonmarked/linkcount/createinit', 'webp.module.views.nonmarked.linkcount.createinit', name="linkcount_createinit"),

    url(r'^nonmarked/linkcount/create', 'webp.module.views.nonmarked.linkcount.create', name="linkcount_create"),

    url(r'^nonmarked/linkcount/delete', 'webp.module.views.nonmarked.linkcount.delete', name="linkcount_delete"),

    url(r'^nonmarked/linkcount/createschedule', 'webp.module.views.nonmarked.linkcount.create_schedule', name="linkcount_create_schedule"),

    url(r'^nonmarked/linkcount', 'webp.module.views.nonmarked.linkcount.index', name="linkcount_index"),

    # ------------------------------------ linkfunction ------------------------------------------------
    url(r'^nonmarked/linkfunction/list', 'webp.module.views.nonmarked.linkfunction.list', name="linkfunction_list"),

    url(r'^nonmarked/linkfunction/show', 'webp.module.views.nonmarked.linkfunction.show', name="linkfunction_show"),

    url(r'^nonmarked/linkfunction/createinit', 'webp.module.views.nonmarked.linkfunction.createinit', name="linkfunction_createinit"),

    url(r'^nonmarked/linkfunction/create', 'webp.module.views.nonmarked.linkfunction.create', name="linkfunction_create"),

    url(r'^nonmarked/linkfunction/delete', 'webp.module.views.nonmarked.linkfunction.delete', name="linkfunction_delete"),

    url(r'^nonmarked/linkfunction/createschedule', 'webp.module.views.nonmarked.linkfunction.create_schedule', name="linkfunction_create_schedule"),

    url(r'^nonmarked/linkfunction', 'webp.module.views.nonmarked.linkfunction.index', name="linkfunction_index"),

    # ------------------------------------ pp ------------------------------------------------
    url(r'^nonmarked/pp/list', 'webp.module.views.nonmarked.pp.list', name="pp_list"),

    url(r'^nonmarked/pp/show', 'webp.module.views.nonmarked.pp.show', name="pp_show"),

    url(r'^nonmarked/pp/createinit', 'webp.module.views.nonmarked.pp.createinit', name="pp_createinit"),

    url(r'^nonmarked/pp/create', 'webp.module.views.nonmarked.pp.create', name="pp_create"),

    url(r'^nonmarked/pp/delete', 'webp.module.views.nonmarked.pp.delete', name="pp_delete"),

    url(r'^nonmarked/pp/createschedule', 'webp.module.views.nonmarked.pp.create_schedule', name="pp_create_schedule"),

    url(r'^nonmarked/pp', 'webp.module.views.nonmarked.pp.index', name="pp_index"),

    # ------------------------------------ fieldcase ----------------------------------------------
    url(r'^nonmarked/fieldcase/list', 'webp.module.views.nonmarked.fieldcase.list', name="fieldcase_list"),

    url(r'^nonmarked/fieldcase/show', 'webp.module.views.nonmarked.fieldcase.show', name="fieldcase_show"),

    url(r'^nonmarked/fieldcase/createinit', 'webp.module.views.nonmarked.fieldcase.createinit', name="fieldcase_createinit"),

    url(r'^nonmarked/fieldcase/createschedule', 'webp.module.views.nonmarked.fieldcase.create_schedule', name="fieldcase_create_schedule"),

    url(r'^nonmarked/fieldcase/delete', 'webp.module.views.nonmarked.fieldcase.delete', name="fieldcase_delete"),

    url(r'^nonmarked/fieldcase/create', 'webp.module.views.nonmarked.fieldcase.create', name="fieldcase_create"),

    url(r'^nonmarked/fieldcase$', 'webp.module.views.nonmarked.fieldcase.index', name="fieldcase_index"),

    # ------------------------------------ googlepr ----------------------------------------------
    url(r'^nonmarked/googlepr/list', 'webp.module.views.nonmarked.googlepr.list', name="googlepr_list"),

    url(r'^nonmarked/googlepr/show', 'webp.module.views.nonmarked.googlepr.show', name="googlepr_show"),

    url(r'^nonmarked/googlepr/createinit', 'webp.module.views.nonmarked.googlepr.createinit', name="googlepr_createinit"),

    url(r'^nonmarked/googlepr/createschedule', 'webp.module.views.nonmarked.googlepr.create_schedule', name="googlepr_create_schedule"),

    url(r'^nonmarked/googlepr/delete', 'webp.module.views.nonmarked.googlepr.delete', name="googlepr_delete"),

    url(r'^nonmarked/googlepr/create', 'webp.module.views.nonmarked.googlepr.create', name="googlepr_create"),

    url(r'^nonmarked/googlepr$', 'webp.module.views.nonmarked.googlepr.index', name="googlepr_index"),
)





if __name__ == "__main__":
    pass

