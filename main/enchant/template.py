pkgname = "enchant"
pkgver = "2.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "aspell-devel",
    "glib-devel",
    "hunspell-devel",
    "icu-devel",
    "libtool-devel",
    "nuspell-devel",
    "unittest-cpp",
]
pkgdesc = "Generic spell checking library"
license = "LGPL-2.1-or-later"
url = "http://rrthomas.github.io/enchant"
source = f"https://github.com/rrthomas/enchant/releases/download/v{pkgver}/enchant-{pkgver}.tar.gz"
sha256 = "e28f98208df5f99320d6a05cd49f83420bf71e69052debe3b343c9bb15c833ed"


@subpackage("enchant-devel")
def _(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _(self):
    return self.default_progs()
