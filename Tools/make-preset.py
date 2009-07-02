#!/usr/bin/env python
# Copyright � 2002 Free Software Foundation, Inc.
# Contributed by Fran�ois Pinard <pinard@iro.umontreal.ca>, 2002.

"""\
Conversion between different charsets, surfaces and structures.

Pre-computation of recoding preset data.
"""

import sys
from Recode import recode

PRESET_PY = 'preset.py'

class Main:

    def main(self, *arguments):
        # Import all modules.
        modules = [getattr(__import__('Recode.' + module_name), module_name)
                   for module_name in arguments]
        # Register aliases into clusters.
        self.clusters = {}
        self.handle_declare(recode.UNICODE_STRING)
        self.handle_declare((recode.TRIVIAL_SURFACE, 'Data'))
        for module in modules:
            try:
                declares = module.declares
            except AttributeError:
                sys.stderr.write("No `declares' in `%s'\n" % module.__file__)
            else:
                for declare in declares:
                    self.handle_declare(declare)
        # Register implied surfaces.
        self.implied = {}
        for module in modules:
            if hasattr(module, 'implied_surfaces'):
                for alias, surface in module.implied_surfaces:
                    self.implied[recode.clean_alias(alias)] = (
                        recode.clean_alias(surface))
        # Register recode methods.
        self.methods = {}
        from types import ClassType
        for module, module_name in zip(modules, arguments):
            for codec_name in dir(module):
                codec = getattr(module, codec_name)
                if not (type(codec) is ClassType
                        and issubclass(codec, recode.Step)
                        and hasattr(codec, 'internal_coding')
                        and hasattr(codec, 'external_coding')):
                    continue
                self.handle_codec(module_name, codec_name, codec)
        # Write out the Python source.
        write = file(PRESET_PY, 'w').write
        write('\n'
              'aliases = {\n')
        items = self.clusters.items()
        items.sort()
        for alias, cluster in items:
            write('    %r: (%r, %r),\n' % (alias, cluster[0],
                                           self.implied.get(alias)))
        write('    }\n'
              '\n'
              'methods = {\n')
        items = self.methods.items()
        items.sort()
        for (before, after), (module_name, codec_name, use_encode) in items:
            write('    (%r, %r): (%r, %r, %r),\n' %
                  (before, after, module_name, codec_name, use_encode))
        write('    }\n')

    def handle_codec(self, module_name, codec_name, codec):
        internal = self.clusters[recode.clean_alias(codec.internal_coding)][0]
        external = self.clusters[recode.clean_alias(codec.external_coding)][0]
        for check, before, after, direction in (
            (codec.encode, internal, external, True),
            (codec.decode, external, internal, False)):
            if check is not None:
                if (before, after) in self.methods:
                    if module_name == 'builtin':
                        sys.stderr.write(
                            "Overriding `%s' by `%s' for `%s..%s'.\n"
                            % (self.methods[before, after][0], module_name,
                               before, after))
                    else:
                        sys.stderr.write(
                            "Overriding `%s' by `%s' for `%s..%s'.\n"
                            % (module_name, self.methods[before, after][0],
                               before, after))
                        continue
                self.methods[before, after] = (
                    module_name, codec_name, direction)

    def handle_declare(self, declare):
        # Split out the official coding name and its aliases.
        if isinstance(declare, str):
            official = declare
            aliases = ()
        else:
            official = declare[0]
            aliases = [recode.clean_alias(alias) for alias in declare[1:]]
        coding = recode.clean_alias(official)
        # Use coding's cluster, create it if necessary.  The first element
        # of a cluster is always the official name, other elements are clean.
        if coding not in self.clusters:
            self.clusters[coding] = [official]
        cluster = self.clusters[coding]
        # Add aliases or clusters to the current cluster.
        for alias in aliases:
            if alias in self.clusters:
                # Add this cluster to the pre-existing alias' cluster.
                # Clean the first element of cluster into a mere alias.
                existing = self.clusters[alias]
                element = recode.clean_alias(cluster[0])
                existing.append(element)
                self.clusters[element] = existing
                for element in cluster[1:]:
                    existing.append(element)
                    self.clusters[element] = existing
                cluster = existing
            else:
                # Add alias to the current cluster.
                cluster.append(alias)
                self.clusters[alias] = cluster

if __name__ == '__main__':
    Main().main(*sys.argv[1:])