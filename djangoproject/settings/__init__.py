import sys

if 'runserver' in sys.argv:
    from .development import *
else:
    from .production import *


# from .base import *

# try:
#     from .development import *
# except:
#     from .production import *


