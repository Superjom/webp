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

    url(r'^nonmarked/fieldstat/createschedule', 'webp.module.views.nonmarked.fieldstat.create_schedule', name="fieldstat_create_schedule"),

    url(r'^nonmarked/fieldstat/delete', 'webp.module.views.nonmarked.fieldstat.delete', name="fieldstat_delete"),

    url(r'^nonmarked/fieldstat/create', 'webp.module.views.nonmarked.fieldstat.create', name="fieldstat_create"),

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

    ####################################### marked ########################################
    # ------------------------------------ tac ------------------------------------------------
    url(r'^marked/markedtac$', 'webp.module.views.marked.tac.index', name="tac_index"),
    url(r'^marked/tac/list$', 'webp.module.views.marked.tac.list', name="tac_list"),
    # create
    url(r'^marked/tac/createinit$', 'webp.module.views.marked.tac.createinit', name="tac_createinit"),

    url(r'^marked/tac/create', 'webp.module.views.marked.tac.create', name="tac_create"),
    # del
    url(r'^marked/tac/del', 'webp.module.views.marked.tac.delete', name="tac_del"),
    
    # update
    url(r'^marked/tac/updateinit', 'webp.module.views.marked.tac.updateinit', name="tac_updateinit"),

    url(r'^marked/tac/update', 'webp.module.views.marked.tac.update', name="tac_update"),

    # ------------------------------------ spam ------------------------------------------------

    url(r'^marked/spam/list?.*', 'webp.module.views.marked.spam.list', name="spam_list"),

    url(r'^marked/spam/show?.*', 'webp.module.views.marked.spam.show', name="spam_show"),

    url(r'^marked/spam/createinit?.*', 'webp.module.views.marked.spam.createinit', name="spam_createinit"),

    url(r'^marked/spam/delete?.*', 'webp.module.views.marked.spam.delete', name="spam_delete"),

    url(r'^marked/spam/createschedule?.*', 'webp.module.views.marked.spam.create_schedule', name="spam_create_schedule"),

    url(r'^marked/spam/create?.*', 'webp.module.views.marked.spam.create', name="spam_create"),

    url(r'^marked/spam?.*', 'webp.module.views.marked.spam.index', name="spam_index"),

    # ------------------------------------ quality ------------------------------------------------

    url(r'^marked/quality/list?.*', 'webp.module.views.marked.quality.list', name="quality_list"),

    url(r'^marked/quality/show?.*', 'webp.module.views.marked.quality.show', name="quality_show"),

    url(r'^marked/quality/createinit?.*', 'webp.module.views.marked.quality.createinit', name="quality_createinit"),

    url(r'^marked/quality/delete?.*', 'webp.module.views.marked.quality.delete', name="quality_delete"),

    url(r'^marked/quality/createschedule?.*', 'webp.module.views.marked.quality.create_schedule', name="quality_create_schedule"),

    url(r'^marked/quality/create?.*', 'webp.module.views.marked.quality.create', name="quality_create"),

    url(r'^marked/quality?.*', 'webp.module.views.marked.quality.index', name="quality_index"),

    ###################################### dcg #################################################
    # ------------------------------------ tac ------------------------------------------------
    url(r'^dcg/dcgtac$', 'webp.module.views.dcg.tac.index', name="tac_index"),
    url(r'^dcg/tac/list$', 'webp.module.views.dcg.tac.list', name="tac_list"),
    # create
    url(r'^dcg/tac/createinit$', 'webp.module.views.dcg.tac.createinit', name="tac_createinit"),

    url(r'^dcg/tac/create', 'webp.module.views.dcg.tac.create', name="tac_create"),
    # del
    url(r'^dcg/tac/del', 'webp.module.views.dcg.tac.delete', name="tac_del"),
    
    # update
    url(r'^dcg/tac/updateinit', 'webp.module.views.dcg.tac.updateinit', name="tac_updateinit"),

    url(r'^dcg/tac/update', 'webp.module.views.dcg.tac.update', name="tac_update"),

    # ------------------------------------ rankla ------------------------------------------------

    url(r'^dcg/rankla/list?.*', 'webp.module.views.dcg.rankla.list', name="rankla_list"),

    url(r'^dcg/rankla/show?.*', 'webp.module.views.dcg.rankla.show', name="rankla_show"),

    url(r'^dcg/rankla/createinit?.*', 'webp.module.views.dcg.rankla.createinit', name="rankla_createinit"),

    url(r'^dcg/rankla/delete?.*', 'webp.module.views.dcg.rankla.delete', name="rankla_delete"),

    url(r'^dcg/rankla/createschedule?.*', 'webp.module.views.dcg.rankla.create_schedule', name="rankla_create_schedule"),

    url(r'^dcg/rankla/create?.*', 'webp.module.views.dcg.rankla.create', name="rankla_create"),

    url(r'^dcg/rankla?.*', 'webp.module.views.dcg.rankla.index', name="rankla_index"),

    # ------------------------------------ rankscore ------------------------------------------------

    url(r'^dcg/rankscore/list?.*', 'webp.module.views.dcg.rankscore.list', name="rankscore_list"),

    url(r'^dcg/rankscore/show?.*', 'webp.module.views.dcg.rankscore.show', name="rankscore_show"),

    url(r'^dcg/rankscore/createinit?.*', 'webp.module.views.dcg.rankscore.createinit', name="rankscore_createinit"),

    url(r'^dcg/rankscore/delete?.*', 'webp.module.views.dcg.rankscore.delete', name="rankscore_delete"),

    url(r'^dcg/rankscore/createschedule?.*', 'webp.module.views.dcg.rankscore.create_schedule', name="rankscore_create_schedule"),

    url(r'^dcg/rankscore/create?.*', 'webp.module.views.dcg.rankscore.create', name="rankscore_create"),

    url(r'^dcg/rankscore?.*', 'webp.module.views.dcg.rankscore.index', name="rankscore_index"),

)




if __name__ == "__main__":
    pass

