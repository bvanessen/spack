##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
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
from spack import *


class DoeNciSplashApp(Package):
    """DOE-NCI Pilot2 Splash App framework"""

    homepage = "https://code.ornl.gov/v33/pilot2-splash-app"
    url      = "https://code.ornl.gov/v33/pilot2-splash-app"

    tags = ['splash-app']

    version('develop')

    depends_on('python@2.7:')

    # Base packages
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-matplotlib ~tk', type=('build', 'run'))
    depends_on('py-mdanalysis@0.16.2:', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))

    # ML
    depends_on('py-theano +gpu', type=('build', 'run'))
    depends_on('py-keras', type=('build', 'run'))
    depends_on('py-scikit-learn@0.18.1:', type=('build', 'run'))


    depends_on('py-mpi4py', type=('build', 'run'))
    depends_on('py-h5py+mpi', type=('build', 'run'))

    # Linters
    depends_on('py-flake8', type=('build', 'run'))
    depends_on('py-pydocstyle', type=('build', 'run'))

    # Unit Testing
    depends_on('py-nose', type=('build', 'run'))
    depends_on('py-coverage', type=('build', 'run'))

    # see #3244, but use external for now
    # depends_on('tensorflow')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix.bin)
