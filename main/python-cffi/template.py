pkgname = "python-cffi"
pkgver = "1.17.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "libffi8-devel",
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["libffi8-devel", "python-devel"]
depends = ["python-pycparser"]
checkdepends = ["python-pycparser", "python-pytest"]
pkgdesc = "C FFI for Python"
license = "MIT"
url = "https://cffi.readthedocs.io"
source = f"$(PYPI_SITE)/c/cffi/cffi-{pkgver}.tar.gz"
sha256 = "1c39c6016c32bc48dd54561950ebd6836e1670f2ae46128f67cf49e789c52824"
# tests crash on loongarch64
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")
