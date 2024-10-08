pkgname = "bubblewrap"
pkgver = "0.10.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "xsltproc", "docbook-xsl-nons"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs", "mount"]
pkgdesc = "Unprivileged sandboxing tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"{url}/releases/download/v{pkgver}/bubblewrap-{pkgver}.tar.xz"
sha256 = "65d92cf44a63a51e1b7771f70c05013dce5bd6b0b2841c4b4be54b0c45565471"
hardening = ["vis", "cfi"]

# seccomp tests fail on aarch64 with efault instead of econnrefused for various assertions
if self.profile().arch != "aarch64":
    checkdepends += ["python-libseccomp"]
