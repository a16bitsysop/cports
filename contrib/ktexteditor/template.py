pkgname = "ktexteditor"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: katedocument_test testAboutToSave() hangs for 5 minutes,
    # txt_diff encoding tests broken similar to alpine but pass in cbuild chroot?
    "katedocument_test|encoding_(utf8|latin15|utf32|utf16|utf32be|utf16be|cyrillic_utf8|cp1251|koi8-r|one-char-latin-15|latin15-with-utf8-bom).txt_diff",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "editorconfig-devel",
    "karchive-devel",
    "kauth-devel",
    "kconfig-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE Full text editor component"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.0-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/ktexteditor/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ktexteditor-{pkgver}.tar.xz"
sha256 = "9991a78fd5cf692964d84210baea472ece56434d924f9e67561b857f8b48c777"
hardening = ["vis"]


@subpackage("ktexteditor-devel")
def _(self):
    self.depends += ["kparts-devel", "syntax-highlighting-devel"]

    return self.default_devel()
