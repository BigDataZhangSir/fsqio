# coding=utf-8
# Copyright 2014 Foursquare Labs Inc. All Rights Reserved.

from __future__ import absolute_import

import os

from pants.backend.jvm.repository import Repository
from pants.base.build_environment import get_buildroot
from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task
from pants.task.task import Task

from fsqio.pants.validate import Tagger, Validate


oss_sonatype_repo = Repository(
  name='oss_sonatype_repo',
  url='https://oss.sonatype.org/#stagingRepositories',
  push_db_basedir=os.path.join(get_buildroot(), 'pushdb'),
)

def build_file_aliases():
  return BuildFileAliases(
    objects={
      'oss_sonatype_repo': oss_sonatype_repo,
    },
  )

def register_goals():
  task(name='tag', action=Tagger).install()
  task(name='validate', action=Validate).install()

  class ForceValidation(Task):
    @classmethod
    def prepare(cls, options, round_manager):
      round_manager.require_data('validated_build_graph')

    def execute(self):
      pass

  task(name='validate-graph', action=ForceValidation).install('gen')
