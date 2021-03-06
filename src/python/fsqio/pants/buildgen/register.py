# coding=utf-8
# Copyright 2016 Foursquare Labs Inc. All Rights Reserved.

from __future__ import absolute_import

from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task

from fsqio.pants.buildgen.buildgen_spindle import BuildgenSpindle
from fsqio.pants.buildgen.core.buildgen import Buildgen
from fsqio.pants.buildgen.core.buildgen_aggregate_targets import BuildgenAggregateTargets
from fsqio.pants.buildgen.core.buildgen_target_bag import BuildgenTargetBag
from fsqio.pants.buildgen.core.buildgen_timestamp import BuildgenTimestamp
from fsqio.pants.buildgen.core.inject_target_bags import BuildgenInjectTargetBags
from fsqio.pants.buildgen.core.map_derived_targets import MapDerivedTargets
from fsqio.pants.buildgen.core.map_sources_to_addresses import MapSourcesToAddresses
from fsqio.pants.buildgen.jvm.map_java_exported_symbols import MapJavaExportedSymbols
from fsqio.pants.buildgen.jvm.map_jvm_symbol_to_source_tree import MapJvmSymbolToSourceTree
from fsqio.pants.buildgen.jvm.map_third_party_jar_symbols import MapThirdPartyJarSymbols
from fsqio.pants.buildgen.jvm.scala.buildgen_scala import BuildgenScala
from fsqio.pants.buildgen.jvm.scala.map_scala_library_used_addresses import (
  MapScalaLibraryUsedAddresses,
)
from fsqio.pants.buildgen.jvm.scala.scala_exported_symbols import MapScalaExportedSymbols
from fsqio.pants.buildgen.jvm.scala.scala_used_symbols import MapScalaUsedSymbols
from fsqio.pants.buildgen.python.buildgen_python import BuildgenPython
from fsqio.pants.buildgen.python.map_python_exported_symbols import MapPythonExportedSymbols


def build_file_aliases():
  return BuildFileAliases(
    targets={
      'buildgen_target_bag': BuildgenTargetBag,
    },
  )

def register_goals():

  task(
    name='map-python-exported-symbols',
    action=MapPythonExportedSymbols,
  ).install()

  task(
    name='map-third-party-jar-symbols',
    action=MapThirdPartyJarSymbols,
  ).install()

  task(
    name='map-scala-exported-symbols',
    action=MapScalaExportedSymbols,
  ).install()

  task(
    name='map-scala-used-symbols',
    action=MapScalaUsedSymbols,
  ).install()

  task(
    name='map-java-exported-symbols',
    action=MapJavaExportedSymbols,
  ).install()

  task(
    name='map-derived-targets',
    action=MapDerivedTargets,
  ).install()

  task(
    name='map-sources-to-addresses-mapper',
    action=MapSourcesToAddresses,
  ).install()

  task(
    name='map-jvm-symbol-to-source-tree',
    action=MapJvmSymbolToSourceTree,
  ).install()

  task(
    name='map-scala-library-used-addresses',
    action=MapScalaLibraryUsedAddresses,
  ).install()

  task(
    name='buildgen',
    action=Buildgen,
  ).install()

  task(
    name='scala',
    action=BuildgenScala,
  ).install('buildgen')

  task(
    name='spindle',
    action=BuildgenSpindle,
  ).install('buildgen')

  task(
    name='python',
    action=BuildgenPython,
  ).install('buildgen')

  task(
    name='add-target-bags',
    action=BuildgenInjectTargetBags,
  ).install('test')

  task(
    name='aggregate-targets',
    action=BuildgenAggregateTargets,
  ).install('buildgen')

  task(
    name='timestamp',
    action=BuildgenTimestamp,
  ).install('buildgen')
