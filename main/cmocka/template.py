pkgname = "cmocka"
pkgver = "1.1.7"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DUNIT_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Unit testing framework in C"
license = "Apache-2.0"
url = "https://cmocka.org"
source = f"{url}/files/{pkgver[:-2]}/cmocka-{pkgver}.tar.xz"
sha256 = "810570eb0b8d64804331f82b29ff47c790ce9cd6b163e98d47a4807047ecad82"


@subpackage("cmocka-devel")
def _(self):
    return self.default_devel()
