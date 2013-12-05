# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013
@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import os
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

#----------------- debug -------------
if __name__ == '__main__':
    import sys
    sys.path.append('/home/chunwei/webp/webp')
    from webp.utils import debug; debug()
#---------------- end  debug -------------

from webp.utils import Util, _debug_print



class Shell(object):
    def __init__(self, module_flag, func_flag, tac_name, log_path=None,  args={}):
        self.module_flag = module_flag
        self.func_flag = func_flag
        self.tac_name = tac_name
        self.log_path = log_path if log_path else self.gen_log_path()
        self.args = args

    def set_args(self, args):
        self.args = args

    def update_args(self, args):
        self.args.update(args)

    def execute(self):
        shell = self.gen_command()
        output = os.system(shell).read()
        _debug_print('shell output: ' + output)
        return True, output

    def gen_command(self):
        shell = [
            os.path.join(Util.INVLINK_HOME,
                self.module_flag, self.func_flag, "%s.sh" %self.func_flag),
            "-e",  Util.INVLINK_HOME,
            "-m", self.module_flag,
            "-f", self.func_flag,
            "-n", self.tac_name, 
            "-l", self.log_path,
            ]

        if not 'k' in self.args and 'v' in self.args:
            raise Exception("error, shell command have no k/v attributes.")

        shell += ["-k", '"%s"'%self.args['k'], "-v", '"%s"'%self.args['v'] ]

        if 'x' in self.args and 'y' in self.args:
            shell += ["-x", '"%s"'%(self.args['x']), "-y", '"%s"'%(self.args['y']) ]

        if 't' in self.args:
            shell += ['-t', self.args['t']]

        shell = ' '.join([str(cmd) for cmd in shell])

        _debug_print('shell: ' + shell)
        return shell

    def gen_log_path(self):
        log_path = os.path.join(
            Util.INVLINK_HOME, 
            self.module_flag,
            self.func_flag,
            "log",
            "%s_%s.log" % (self.tac_name.strip(), Util.get_date() ),
            )
        return log_path


if __name__ == "__main__":
    shell = Shell(
        '>module_flag',
        '>func_flag',
        '>tac_name',
        '>log_path',
        args = {
            'k': '>k',
            'v': '>v',
            }
        )
    print shell.gen_command()

