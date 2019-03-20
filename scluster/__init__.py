import os

from . import aws_backend
from . import aws_util
from . import util
from . import local_backend
from . import backend  # TODO: remove?

from .scluster import get_backend
from .scluster import set_backend
from .scluster import running_locally

from .scluster import use_aws
from .scluster import use_local

from .scluster import make_task
from .scluster import make_job
from .scluster import make_run
from .scluster import get_zone
from .scluster import get_region
from .scluster import set_logdir_root
from .scluster import get_logdir_root

import logging
logging.getLogger("botocore").setLevel(logging.ERROR)

# set default backend from environment
if 'NCLUSTER_BACKEND' in os.environ:
  set_backend(os.environ['NCLUSTER_BACKEND'])
else:
  set_backend('local')

util.install_pdb_handler()  # CTRL+\ drops into pdb
