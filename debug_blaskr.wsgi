activate_this = '/home/kfl/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from blaskr import blaskr

# If you need debug information you can make a DebuggedApplication

from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(blaskr.app, True)
