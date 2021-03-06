# coding=utf-8
# Copyright 2013 Foursquare Labs Inc. All Rights Reserved.

from __future__ import (
  absolute_import,
  division,
  generators,
  nested_scopes,
  print_function,
  unicode_literals,
  with_statement,
)

import os
import time

from pants.task.task import Task


class BuildgenTimestamp(Task):
  """Log when buildgen was last ran in a findable place"""

  def execute(self):
    with open(os.path.join(self.get_options().pants_workdir, '.buildgen_timestamp'), 'w') as f:
      f.write(str(int(time.time())))
