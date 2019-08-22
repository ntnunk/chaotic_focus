import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_PATH = os.path.join(basedir, 'tmp')
ALLOWED_EXTENSIONS = set(['md'])
#MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # Max file length for upload is 16MB

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
