from split_settings.tools import include

include('base.py')

try:
    from .development import *
except:
    from .production import *
