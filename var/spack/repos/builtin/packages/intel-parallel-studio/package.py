##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack.util.prefix import Prefix
from spack import *
import os


class IntelParallelStudio(IntelPackage):
    """Intel Parallel Studio."""

    homepage = "https://software.intel.com/en-us/intel-parallel-studio-xe"

    version('professional.2017.4', '27398416078e1e4005afced3e9a6df7e',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11537/parallel_studio_xe_2017_update4.tgz')
    version('cluster.2017.4',      '27398416078e1e4005afced3e9a6df7e',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11537/parallel_studio_xe_2017_update4.tgz')
    version('composer.2017.4',     'd03d351809e182c481dc65e07376d9a2',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11541/parallel_studio_xe_2017_update4_composer_edition.tgz')
    version('professional.2017.3', '691874735458d3e88fe0bcca4438b2a9',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11460/parallel_studio_xe_2017_update3.tgz')
    version('cluster.2017.3',      '691874735458d3e88fe0bcca4438b2a9',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11460/parallel_studio_xe_2017_update3.tgz')
    version('composer.2017.3',     '52344df122c17ddff3687f84ceb21623',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11464/parallel_studio_xe_2017_update3_composer_edition.tgz')
    version('professional.2017.2', '70e54b33d940a1609ff1d35d3c56e3b3',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11298/parallel_studio_xe_2017_update2.tgz')
    version('cluster.2017.2',      '70e54b33d940a1609ff1d35d3c56e3b3',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11298/parallel_studio_xe_2017_update2.tgz')
    version('composer.2017.2',     '2891ab1ece43eb61b6ab892f07c47f01',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11302/parallel_studio_xe_2017_update2_composer_edition.tgz')
    version('professional.2017.1', '7f75a4a7e2c563be778c377f9d35a542',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/10973/parallel_studio_xe_2017_update1.tgz')
    version('cluster.2017.1',      '7f75a4a7e2c563be778c377f9d35a542',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/10973/parallel_studio_xe_2017_update1.tgz')
    version('composer.2017.1',     '1f31976931ed8ec424ac7c3ef56f5e85',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/10978/parallel_studio_xe_2017_update1_composer_edition.tgz')
    version('professional.2017.0', '34c98e3329d6ac57408b738ae1daaa01',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9651/parallel_studio_xe_2017.tgz')
    version('cluster.2017.0',      '34c98e3329d6ac57408b738ae1daaa01',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9651/parallel_studio_xe_2017.tgz')
    version('composer.2017.0',     'b67da0065a17a05f110ed1d15c3c6312',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9656/parallel_studio_xe_2017_composer_edition.tgz')
    version('professional.2016.4', '16a641a06b156bb647c8a56e71f3bb33',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9781/parallel_studio_xe_2016_update4.tgz')
    version('cluster.2016.4',      '16a641a06b156bb647c8a56e71f3bb33',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9781/parallel_studio_xe_2016_update4.tgz')
    version('composer.2016.4',      '2bc9bfc9be9c1968a6e42efb4378f40e',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9785/parallel_studio_xe_2016_composer_edition_update4.tgz')
    version('professional.2016.3', 'eda19bb0d0d19709197ede58f13443f3',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9061/parallel_studio_xe_2016_update3.tgz')
    version('cluster.2016.3',      'eda19bb0d0d19709197ede58f13443f3',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9061/parallel_studio_xe_2016_update3.tgz')
    version('composer.2016.3',     '3208eeabee951fc27579177b593cefe9',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9063/parallel_studio_xe_2016_composer_edition_update3.tgz')
    version('professional.2016.2', '70be832f2d34c9bf596a5e99d5f2d832',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8676/parallel_studio_xe_2016_update2.tgz')
    version('cluster.2016.2',      '70be832f2d34c9bf596a5e99d5f2d832',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8676/parallel_studio_xe_2016_update2.tgz')
    version('composer.2016.2',     '1133fb831312eb519f7da897fec223fa',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8680/parallel_studio_xe_2016_composer_edition_update2.tgz')
    version('professional.2015.6', 'd460f362c30017b60f85da2e51ad25bf',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8469/parallel_studio_xe_2015_update6.tgz')
    version('cluster.2015.6',      'd460f362c30017b60f85da2e51ad25bf',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8469/parallel_studio_xe_2015_update6.tgz')
    version('composer.2015.6',      'da9f8600c18d43d58fba0488844f79c9',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/8432/l_compxe_2015.6.233.tgz')

    # Generic Variants
    variant('rpath',    default=True,
            description='Add rpath to .cfg files')
    variant('newdtags', default=False,
            description='Allow use of --enable-new-dtags in MPI wrappers')
    variant('shared',   default=True,
            description='Builds shared library')
    variant('ilp64',    default=False,
            description='64 bit integers')
    variant('openmp',   default=False,
            description='OpenMP multithreading layer')
    variant('all',      default=False,
            description='Install all components of the requested edition')

    # Components available in all editions
    variant('daal', default=True,
            description='Install the Intel DAAL libraries')
    variant('gdb',  default=False,
            description='Install the Intel Debugger for Heterogeneous Compute')
    variant('ipp',  default=True,
            description='Install the Intel IPP libraries')
    variant('mkl',  default=True,
            description='Install the Intel MKL library')
    variant('mpi',  default=True,
            description='Install the Intel MPI library')
    variant('tbb',  default=True,
            description='Install the Intel TBB libraries')

    # Components only available in the Professional and Cluster Editions
    variant('advisor',   default=False,
            description='Install the Intel Advisor')
    variant('clck',      default=False,
            description='Install the Intel Cluster Checker')
    variant('inspector', default=False,
            description='Install the Intel Inspector')
    variant('itac',      default=False,
            description='Install the Intel Trace Analyzer and Collector')
    variant('vtune',     default=False,
            description='Install the Intel VTune Amplifier XE')

    provides('daal', when='+daal')
    provides('daal', when='+all')

    provides('ipp', when='+ipp')
    provides('ipp', when='+all')

    provides('mkl',       when='+mkl')
    provides('mkl',       when='+all')
    provides('blas',      when='+mkl')
    provides('blas',      when='+all')
    provides('lapack',    when='+mkl')
    provides('lapack',    when='+all')
    provides('scalapack', when='+mkl')
    provides('scalapack', when='+all')

    provides('mpi', when='+mpi')
    provides('mpi', when='+all')

    provides('tbb', when='+tbb')
    provides('tbb', when='+all')

    # The following components are not available in the Composer Edition
    conflicts('+advisor',   when='@composer.0:composer.9999')
    conflicts('+clck',      when='@composer.0:composer.9999')
    conflicts('+inspector', when='@composer.0:composer.9999')
    conflicts('+itac',      when='@composer.0:composer.9999')
    conflicts('+vtune',     when='@composer.0:composer.9999')

    @property
    def blas_libs(self):
        spec = self.spec
        prefix = self.prefix
        shared = '+shared' in spec

        if '+ilp64' in spec:
            mkl_integer = ['libmkl_intel_ilp64']
        else:
            mkl_integer = ['libmkl_intel_lp64']

        mkl_threading = ['libmkl_sequential']

        if '+openmp' in spec:
            if '%intel' in spec:
                mkl_threading = ['libmkl_intel_thread', 'libiomp5']
            else:
                mkl_threading = ['libmkl_gnu_thread']

        # TODO: TBB threading: ['libmkl_tbb_thread', 'libtbb', 'libstdc++']

        mkl_root = join_path(prefix, 'mkl', 'lib', 'intel64')

        mkl_libs = find_libraries(
            mkl_integer + ['libmkl_core'] + mkl_threading,
            root=mkl_root,
            shared=shared
        )

        # Intel MKL link line advisor recommends these system libraries
        system_libs = find_system_libraries(
            ['libpthread', 'libm', 'libdl'],
            shared=shared
        )

        return mkl_libs + system_libs

    @property
    def lapack_libs(self):
        return self.blas_libs

    @property
    def scalapack_libs(self):
        libnames = ['libmkl_scalapack']
        if self.spec.satisfies('^openmpi'):
            libnames.append('libmkl_blacs_openmpi')
        elif self.spec.satisfies('^mpich@1'):
            libnames.append('libmkl_blacs')
        elif self.spec.satisfies('^mpich@2:'):
            libnames.append('libmkl_blacs_intelmpi')
        elif self.spec.satisfies('^mvapich2'):
            libnames.append('libmkl_blacs_intelmpi')
        elif self.spec.satisfies('^mpt'):
            libnames.append('libmkl_blacs_sgimpt')
        # TODO: ^intel-parallel-studio can mean intel mpi, a compiler or a lib
        # elif self.spec.satisfies('^intel-parallel-studio'):
        #     libnames.append('libmkl_blacs_intelmpi')
        else:
            raise InstallError("No MPI found for scalapack")

        shared = True if '+shared' in self.spec else False
        integer = 'ilp64' if '+ilp64' in self.spec else 'lp64'
        libs = find_libraries(
            ['{0}_{1}'.format(l, integer) for l in libnames],
            root=join_path(self.prefix, 'mkl', 'lib', 'intel64'),
            shared=shared
        )
        return libs

    @property
    def components(self):
        spec = self.spec
        edition = self.version[0]

        if '+all' in spec:
            return ['ALL']

        # Intel(R) Compilers
        components = [
            # Common files
            'intel-comp-',
            'intel-openmp',

            # C/C++
            'intel-icc',

            # Fortran
            'intel-ifort',

            # Parallel Studio Documentation and Licensing Files
            'intel-psxe',
        ]

        # Intel(R) Parallel Studio XE Suite Files and Documentation
        if edition == 'cluster':
            components.append('intel-icsxe')
        elif edition == 'professional':
            components.extend(['intel-ips', 'intel-ipsc', 'intel-ipsf'])
        elif edition == 'composer':
            components.extend([
                'intel-compxe', 'intel-ccompxe', 'intel-fcompxe'
            ])

        # Intel(R) Data Analytics Acceleration Library
        if '+daal' in spec:
            components.append('intel-daal')

        # Intel(R) Debugger for Heterogeneous Compute
        if '+gdb' in spec:
            components.append('intel-gdb')

        # Intel(R) Integrated Performance Primitives
        if '+ipp' in spec:
            components.extend(['intel-ipp', 'intel-crypto-ipp'])

        # Intel(R) Math Kernel Library
        if '+mkl' in spec:
            components.append('intel-mkl')

        # Intel(R) MPI Library
        if '+mpi' in spec:
            components.extend(['intel-mpi', 'intel-mpirt', 'intel-imb'])

        # Intel(R) Threading Building Blocks
        if '+tbb' in spec:
            components.append('intel-tbb')

        # Intel(R) Advisor
        if '+advisor' in spec:
            components.append('intel-advisor')

        # Intel(R) Cluster Checker
        if '+clck' in spec:
            components.append('intel_clck')

        # Intel(R) Inspector
        if '+inspector' in spec:
            components.append('intel-inspector')

        # Intel(R) Trace Analyzer and Collector
        if '+itac' in spec:
            components.extend(['intel-itac', 'intel-ta', 'intel-tc'])

        # Intel(R) VTune(TM) Amplifier XE
        if '+vtune' in spec:
            components.append('intel-vtune-amplifier-xe')

        return components

    @property
    def bin_dir(self):
        """The relative path to the bin directory with symlinks resolved."""

        bin_path = os.path.join(self.prefix.bin, 'icc')
        absolute_path = os.path.realpath(bin_path)  # resolve symlinks
        relative_path = os.path.relpath(absolute_path, self.prefix)
        return os.path.dirname(relative_path)

    @property
    def lib_dir(self):
        """The relative path to the lib directory with symlinks resolved."""

        lib_path = os.path.join(self.prefix.lib, 'intel64', 'libimf.a')
        absolute_path = os.path.realpath(lib_path)  # resolve symlinks
        relative_path = os.path.relpath(absolute_path, self.prefix)
        return os.path.dirname(relative_path)

    @property
    def license_files(self):
        spec = self.spec

        directories = [
            'Licenses',
            self.bin_dir
        ]

        if '+tools' in spec and (spec.satisfies('@cluster') or
                                 spec.satisfies('@professional')):
            advisor_dir = 'advisor_xe/licenses'
            inspector_dir = 'inspector_xe/licenses'
            vtune_amplifier_dir = 'vtune_amplifier_xe/licenses'

            year = self.version[1]
            if year >= 2017:
                advisor_dir = 'advisor/licenses'
                inspector_dir = 'inspector/licenses'

            directories.extend([
                advisor_dir,
                inspector_dir,
                vtune_amplifier_dir
            ])

        # if ('+all' in spec or '+mpi' in spec) and spec.satisfies('@cluster'):
        #     for ifile in os.listdir(os.path.join(self.prefix, 'itac')):
        #         if os.path.isdir(os.path.join(self.prefix, 'itac', ifile)):
        #             directories.append(os.path.join(
        #                 self.prefix, 'itac', ifile))
        #         if os.path.isdir(os.path.join(self.prefix, 'itac',
        #                                       ifile, 'intel64')):
        #             directories.append(os.path.join(self.prefix, 'itac',
        #                                ifile, 'intel64'))
        #
        # This is the same as itac/2017.3.030/intel64/
        # Allow glob characters in license_files?

        return [os.path.join(dir, 'license.lic') for dir in directories]

    @run_after('install')
    def filter_compiler_wrappers(self):
        spec = self.spec

        if ('+all' in spec or '+mpi' in spec) and spec.satisfies('@cluster'):
            if '~newdtags' in spec:
                wrappers = [
                    'mpif77', 'mpif90', 'mpigcc', 'mpigxx',
                    'mpiicc', 'mpiicpc', 'mpiifort'
                ]
                wrapper_paths = []
                for root, dirs, files in os.walk(spec.prefix):
                    for name in files:
                        if name in wrappers:
                            wrapper_paths.append(os.path.join(spec.prefix,
                                                              root, name))
                for wrapper in wrapper_paths:
                    filter_file('-Xlinker --enable-new-dtags', ' ',
                                wrapper, string=True)

    @run_after('install')
    def rpath_configuration(self):
        spec = self.spec

        if '+rpath' in spec:
            lib_dir = os.path.join(self.prefix, self.lib_dir)
            for compiler in ['icc', 'icpc', 'ifort']:
                cfgfilename = os.path.join(
                    self.prefix, self.bin_dir, '{0}.cfg'.format(compiler))
                with open(cfgfilename, 'w') as f:
                    f.write('-Xlinker -rpath -Xlinker {0}\n'.format(lib_dir))

    def setup_environment(self, spack_env, run_env):
        """Adds environment variables to the generated module file.

        These environment variables come from running:

        .. code-block:: console

           $ source parallel_studio_xe_2017/bin/psxevars.sh intel64
        """
        spec   = self.spec
        prefix = self.prefix

        edition = self.version[0]
        year    = self.version[1]

        # Generic environment variables
        compiler_root = Prefix(join_path(
            prefix, 'compilers_and_libraries', 'linux', 'compiler'))

        run_env.prepend_path('LD_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'intel64_lin'))
        run_env.prepend_path('LD_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'intel64'))
        run_env.prepend_path('LIBRARY_PATH',
                             join_path(compiler_root.lib, 'intel64_lin'))
        run_env.prepend_path('MANPATH', join_path(prefix.man, 'common'))
        run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'intel64_lin_mic'))
        run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'mic'))
        run_env.prepend_path('MIC_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'intel64_lin_mic'))
        run_env.prepend_path('MIC_LIBRARY_PATH',
                             join_path(compiler_root.lib, 'mic'))
        run_env.prepend_path('NLSPATH', join_path(
            compiler_root.lib, 'intel64', 'locale', '%l_%t', '%N'))
        run_env.prepend_path('PATH', join_path(
            prefix, 'compilers_and_libraries', 'linux', 'bin', 'intel64'))

        # Components available in all editions
        if '+daal' in spec or '+all' in spec:
            daal_root = Prefix(join_path(
                prefix, 'compilers_and_libraries', 'linux', 'daal'))

            run_env.prepend_path('CLASSPATH', join_path(
                daal_root.lib, 'daal.jar'))
            run_env.prepend_path('CPATH', daal_root.include)
            run_env.set('DAALROOT', daal_root)
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(daal_root.lib, 'intel64_lin'))
            run_env.prepend_path('LIBRARY_PATH',
                                 join_path(daal_root.lib, 'intel64_lin'))

        if '+gdb' in spec or '+all' in spec:
            debugger_root = Prefix(join_path(
                prefix, 'debugger_{0}'.format(year)))
            debugger_doc_root = Prefix(join_path(
                prefix, 'documentation_{0}'.format(year), 'en', 'debugger'))

            run_env.set('GDB_CROSS', join_path(
                debugger_root, 'gdb', 'intel64_mic', 'bin', 'gdb-mic'))
            run_env.set('GDBSERVER_MIC', join_path(
                debugger_root, 'gdb', 'targets', 'mic', 'bin', 'gdbserver'))
            run_env.prepend_path('INFOPATH', join_path(
                debugger_doc_root, 'gdb-igfx', 'info'))
            run_env.prepend_path('INFOPATH', join_path(
                debugger_doc_root, 'gdb-mic', 'info'))
            run_env.prepend_path('INFOPATH', join_path(
                debugger_doc_root, 'gdb-ia', 'info'))
            run_env.set('INTEL_PYTHONHOME',
                        join_path(debugger_root, 'python', 'intel64'))
            run_env.prepend_path('LD_LIBRARY_PATH', join_path(
                debugger_root, 'libipt', 'intel64', 'lib'))
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(debugger_root, 'iga', 'lib'))
            run_env.prepend_path('MANPATH', join_path(
                debugger_doc_root, 'gdb-igfx', 'man'))
            run_env.prepend_path('MANPATH', join_path(
                debugger_doc_root, 'gdb-mic', 'man'))
            run_env.prepend_path('MANPATH', join_path(
                debugger_doc_root, 'gdb-ia', 'man'))
            run_env.set('MPM_LAUNCHER', join_path(
                debugger_root, 'mpm', 'mic', 'bin', 'start_mpm.sh'))
            run_env.prepend_path('NLSPATH',
                                 join_path(debugger_root, 'gdb', 'intel64',
                                           'share', 'locale', '%l_%t', '%N'))
            run_env.prepend_path('NLSPATH',
                                 join_path(debugger_root, 'gdb', 'intel64_mic',
                                           'share', 'locale', '%l_%t', '%N'))
            run_env.prepend_path('PATH', join_path(
                debugger_root, 'gdb', 'intel64_mic', 'bin'))

        if '+ipp' in spec or '+all' in spec:
            ipp_root = Prefix(join_path(
                prefix, 'compilers_and_libraries', 'linux', 'ipp'))

            run_env.prepend_path('CPATH', ipp_root.include)
            run_env.set('IPPROOT', ipp_root)
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(ipp_root.lib, 'intel64'))
            run_env.prepend_path('LIBRARY_PATH',
                                 join_path(ipp_root.lib, 'intel64'))
            run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                                 join_path(ipp_root.lib, 'mic'))

        if '+mkl' in spec or '+all' in spec:
            mkl_root = Prefix(join_path(
                prefix, 'compilers_and_libraries', 'linux', 'mkl'))

            run_env.prepend_path('CPATH', mkl_root.include)
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(mkl_root.lib, 'intel64_lin'))
            run_env.prepend_path('LIBRARY_PATH',
                                 join_path(mkl_root.lib, 'intel64_lin'))
            run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                                 join_path(mkl_root.lib, 'intel64_lin_mic'))
            run_env.prepend_path('MIC_LIBRARY_PATH',
                                 join_path(mkl_root.lib, 'intel64_lin_mic'))
            run_env.set('MKLROOT', mkl_root)
            run_env.prepend_path('NLSPATH', join_path(
                mkl_root.lib, 'intel64_lin', 'locale', '%l_%t', '%N'))

        if '+mpi' in spec or '+all' in spec:
            mpi_root = Prefix(join_path(
                prefix, 'compilers_and_libraries', 'linux', 'mpi'))

            run_env.prepend_path('CLASSPATH', join_path(
                mpi_root, 'intel64', 'lib', 'mpi.jar'))
            run_env.set('I_MPI_ROOT', mpi_root)
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(mpi_root, 'mic', 'lib'))
            run_env.prepend_path('LD_LIBRARY_PATH',
                                 join_path(mpi_root, 'intel64', 'lib'))
            run_env.prepend_path('MANPATH', mpi_root.man)
            run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                                 join_path(mpi_root, 'mic', 'lib'))
            run_env.prepend_path('MIC_LIBRARY_PATH',
                                 join_path(mpi_root, 'mic', 'lib'))
            run_env.prepend_path('PATH', join_path(mpi_root, 'intel64', 'bin'))

        if '+tbb' in spec or '+all' in spec:
            tbb_root = Prefix(join_path(
                prefix, 'compilers_and_libraries', 'linux', 'tbb'))

            run_env.prepend_path('CPATH', tbb_root.include)
            run_env.prepend_path('LD_LIBRARY_PATH', join_path(
                tbb_root.lib, 'intel64', 'gcc4.4'))
            run_env.prepend_path('LIBRARY_PATH', join_path(
                tbb_root.lib, 'intel64', 'gcc4.4'))
            run_env.prepend_path('MIC_LD_LIBRARY_PATH',
                                 join_path(tbb_root.lib, 'mic'))
            run_env.prepend_path('MIC_LIBRARY_PATH',
                                 join_path(tbb_root.lib, 'mic'))
            run_env.set('TBBROOT', tbb_root)

        if edition == 'composer':
            return

        # Components only available in the Professional and Cluster Editions
        if '+advisor' in spec or '+all' in spec:
            advisor_root = Prefix(join_path(prefix, 'advisor'))

            run_env.set('ADVISOR_{0}_DIR'.format(year), advisor_root)
            run_env.prepend_path('PATH', advisor_root.bin64)
            run_env.prepend_path('PYTHONPATH',
                                 join_path(advisor_root, 'pythonapi'))

        if '+inspector' in spec or '+all' in spec:
            inspector_root = Prefix(join_path(prefix, 'inspector'))

            run_env.set('INSPECTOR_{0}_DIR'.format(year), inspector_root)
            run_env.prepend_path('PATH', inspector_root.bin64)

        if '+itac' in spec or '+all' in spec:
            itac_root = Prefix(join_path(prefix, 'itac_{0}'.format(year)))

            run_env.prepend_path('LD_LIBRARY_PATH', join_path(
                itac_root, 'intel64', 'slib'))
            run_env.prepend_path('LD_LIBRARY_PATH', join_path(
                itac_root, 'mic', 'slib'))
            run_env.prepend_path('MANPATH', itac_root.man)
            run_env.set('MPS_INTEL_LIBITTNOTIFY64', 'libmps.so')
            run_env.set('MPS_KMP_FORKJOIN_FRAMES_MODE', '3')
            run_env.set('MPS_LD_PRELOAD', 'libmps.so')
            run_env.set('MPS_STAT_DIR_POSTFIX', '_%D-%T')
            run_env.set('MPS_STAT_ENABLE_IDLE', 'I_MPI_PVAR_IDLE')
            run_env.set('MPS_STAT_ENABLE_IDLE_VAL', '1')
            run_env.set('MPS_STAT_LEVEL', '5')
            run_env.set('MPS_STAT_MESSAGES', '1')
            run_env.set('MPS_TOOL_ROOT', itac_root)
            run_env.prepend_path('PATH',
                                 join_path(itac_root, 'intel64', 'bin'))
            run_env.set('VT_ADD_LIBS',
                        '-ldwarf -lelf -lvtunwind -lm -lpthread')
            run_env.set('VT_ARCH', 'intel64')
            run_env.set('VT_LIB_DIR', join_path(itac_root, 'intel64', 'lib'))
            run_env.set('VT_MPI', 'impi4')
            run_env.set('VT_ROOT', itac_root)
            run_env.set('VT_SLIB_DIR', join_path(itac_root, 'intel64', 'slib'))

        if '+vtune' in spec or '+all' in spec:
            vtune_root = Prefix(join_path(prefix, 'vtune_amplifier_xe'))

            run_env.prepend_path('PATH', vtune_root.bin64)
            run_env.set('VTUNE_AMPLIFIER_XE_{0}_DIR'.format(year), vtune_root)

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('I_MPI_CC',  spack_cc)
        spack_env.set('I_MPI_CXX', spack_cxx)
        spack_env.set('I_MPI_F77', spack_fc)
        spack_env.set('I_MPI_F90', spack_f77)
        spack_env.set('I_MPI_FC',  spack_fc)

    def setup_dependent_package(self, module, dep_spec):
        # Check for presence of bin64 or bin directory
        if os.path.isdir(self.prefix.bin):
            bindir = self.prefix.bin
        elif os.path.isdir(self.prefix.bin64):
            bindir = self.prefix.bin64
        else:
            raise RuntimeError('No suitable bindir found')

        self.spec.mpicc  = join_path(bindir, 'mpicc')
        self.spec.mpicxx = join_path(bindir, 'mpic++')
        self.spec.mpifc  = join_path(bindir, 'mpif90')
        self.spec.mpif77 = join_path(bindir, 'mpif77')
