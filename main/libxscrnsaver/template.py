pkgname = "libxscrnsaver"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel"]
pkgdesc = "X Screensaver Library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXScrnSaver-{pkgver}.tar.gz"
sha256 = "0656b2630475104d6df75d91ebb8e0153e61d14e9871ef1f403bcda4a62a838a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxscrnsaver-devel")
def _(self):
    return self.default_devel()
