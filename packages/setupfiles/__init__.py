#!/usr/bin/env python
import distutils
from distutils import dist # python2.6
from setupfiles.dist import DistributionMetadata
from setupfiles.setup import setup

__all__ = ["setup"]

distutils.dist.DistributionMetadata = DistributionMetadata
#dist.DistributionMetadata = DistributionMetadata
distutils.core.setup = setup
