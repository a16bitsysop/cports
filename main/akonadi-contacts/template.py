pkgname = "akonadi-contacts"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-devel",
    "grantleetheme-devel",
    "kcodecs-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kmime-devel",
    "kservice-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
    "ktextwidgets-devel",
    "kxmlgui-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi contacts libraries"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/akonadi-contacts/html/index.html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-contacts-{pkgver}.tar.xz"
)
sha256 = "38386e1b077f8ad896b79083c2ba0c70558920d86ca6ddc45a96a8889c7717db"


@subpackage("akonadi-contacts-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "grantleetheme-devel",
        "kcontacts-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
