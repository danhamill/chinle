import pathlib
class Load_Environment(object):

    def __init__(self):
        self.find_cur_dir()


    def in_notebook(self):
        try:
            from IPython import get_ipython
            if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
                return False
        except ImportError:
            return False
        except AttributeError:
            return False
        return True
    
    def find_cur_dir(self):
        if self.in_notebook():
            cur_dir = pathlib.Path().resolve().parents[0]
        else:
            cur_dir = pathlib.Path().resolve()
        
        self.cur_dir = cur_dir
        return cur_dir