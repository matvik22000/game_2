import sys
from winpython import wppm, utils

try:
    dist = wppm.Distribution(sys.prefix)
    package = wppm.Package(pathtoexefile)
    dist.install(package)
except:
    raise Exception("Unable to install the package.")