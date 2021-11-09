pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

depends = [
    "base-files", "apk-chimera-hooks", "musl-devel", "elftoolchain", "llvm",
    "clang", "lld", "apk-tools", "bsdutils-extra", "bsdgrep", "bsdgzip",
    "bsdpatch", "bsdsed", "bsddiff", "bmake", "bsdtar", "dash", "mksh-static",
    "awk", "ncurses", "util-linux-cbuild", "tzdata", "fakeroot",
]

options = ["bootstrap", "brokenlinks"]

if current.stage > 1:
    depends += ["ccache"]
