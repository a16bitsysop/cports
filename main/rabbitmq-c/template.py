pkgname = "rabbitmq-c"
pkgver = "0.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_STATIC_LIBS=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_SSL_SUPPORT=ON",
    "-DBUILD_TESTS=ON",
    "-DBUILD_TOOLS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen", "xmlto"]
makedepends = ["openssl-devel", "popt-devel"]
pkgdesc = "RabbitMQ C client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/alanxz/rabbitmq-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "839b28eae20075ac58f45925fe991d16a3138cbde015db0ee11df1acb1c493df"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rabbitmq-c-devel")
def _(self):
    return self.default_devel()


@subpackage("rabbitmq-c-progs")
def _(self):
    return self.default_progs()
