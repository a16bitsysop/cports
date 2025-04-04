pkgname = "libxpresent"
pkgver = "1.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrandr-devel"]
pkgdesc = "XPresent extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpresent-{pkgver}.tar.gz"
sha256 = "8ebf8567a8f6afe5a64275a2ecfd4c84e957970c27299d964350f60be9f3541d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxpresent-devel")
def _(self):
    return self.default_devel()
