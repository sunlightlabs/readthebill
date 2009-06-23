DATABASE_ENGINE = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

import os.path
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'))

# path to the receive URL for the TransparencyCorps photo-gathering task
TCORPS_TASK_URL = ''

# The flickr ID for the account you're using to show gathered photos
FLICKR_ID = ''

# the tag that gathered photos are using
FLICKR_TAG = 'readthebill'