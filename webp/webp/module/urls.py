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

def gen_tac_urls(module, tac=None, taclist=[
        'list', 'show', 'createinit', 'create', 'delete',
        'createschedule', 'create']):
    def gen_tac(tac):
        if tac:
            return url(
                r'^%s/tac/%s?.*' % (module, tac), 
            'webp.module.views.%s.%s.%s' % ( module, tac, tac))
        return url(
            r'^%s/tac' % (module), 
        'webp.module.views.%s.%s.%s' % ( module, tac, tac))

    ''' two models:  tac or taclist '''
    if tac is None:
        return [gen_tac(tac) for tac in taclist]
    return gen_tac(tac)


def gen_func_url_list(module, tac):

    def gen_func(tac):
        return url(
        (r'^%s/%s/%s?.*' if func else r'^%s/%s') % (module, tac, func), 
        'webp.module.views.%s.%s.%s' % ( module, tac, func)
        )

    func_urls = [gen_func(func) for func in ('list', 'show', 'createinit', 'delete', 'create', 'index')]
    return func_urls


url_struct = {
    'nonmarked': {
        'tac': 'nonmarkedtac',
        'tacs': [
            'anchorstat',
            'fieldstat',
            'fieldcase',
            'googlepr',
            'linkcount',
            'linkfunction',
            'pp', ],
    },
    'marked': {
        'tac': 'markedtac',
        'tacs': [
            'quality',
            'spam',
            ],
    },
    'dcg': {
        'tac': 'dcgtac',
        'tacs': [
            'rankla',
            'rankscore',
            ]
    }
}

url_list = []

for module,dic in url_struct:
    tac_ctrl_name = dic['tac']
    tacs = dic['tacs']
    tac_ctrl_urls = gen_tac_urls(module)
    tac_func_urls = []
    for tac in tacs:
        tac_func_urls += gen_func_url_list(module, tac)
    url_list += tac_ctrl_urls + tac_func_urls

urlpatterns = patterns('', *url_list)




if __name__ == "__main__":
    pass

