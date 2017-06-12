activate_this = '/home/kfl/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from blaskr import blaskr

application = blaskr.app # The WGSI application is blask.app
