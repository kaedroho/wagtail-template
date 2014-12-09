from .wsgi import application as base_application


# Add dj-static middleware
from dj_static import Cling, MediaCling

application = Cling(MediaCling(base_application))
