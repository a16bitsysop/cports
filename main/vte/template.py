pkgname = "vte"
pkgver = "0.80.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-D_systemd=false",
    "-Dgir=true",
    "-Dvapi=true",
    "-Dgtk4=true",
]
hostmakedepends = [
    "bash",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "fribidi-devel",
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "icu-devel",
    "linux-headers",
    "lz4-devel",
    "pango-devel",
    "pcre2-devel",
    "vala-devel",
    "zlib-ng-compat-devel",
]
renames = ["vte-common"]
pkgdesc = "Gtk terminal widget"
subdesc = "common files"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = [
    f"$(GNOME_SITE)/vte/{pkgver[: pkgver.rfind('.')]}/vte-{pkgver}.tar.xz",
    "https://github.com/fastfloat/fast_float/archive/refs/tags/v8.0.2.tar.gz",
]
source_paths = [".", "subprojects/fast_float"]
sha256 = [
    "2e596fd3fbeabb71531662224e71f6a2c37f684426136d62854627276ef4f699",
    "e14a33089712b681d74d94e2a11362643bd7d769ae8f7e7caefe955f57f7eacd",
]
# assert in meson
options = ["!lto", "!cross"]

tool_flags = {
    "CFLAGS": ["-Wno-cast-function-type-strict"],
    "CXXFLAGS": [
        "-Wno-cast-function-type-strict",
        # these are bad but also very noisy...
        "-Wno-cast-align",
        "-Wno-float-equal",
    ],
}


def post_extract(self):
    self.mv(
        "subprojects/packagefiles/fast_float/meson.build",
        "subprojects/fast_float",
    )


@subpackage("vte-gtk3")
def _(self):
    self.subdesc = "Gtk+3"
    self.depends = [self.parent]
    return [
        "usr/lib/libvte-2.91.so.*",
        "usr/lib/girepository-1.0/Vte-2.91.typelib",
    ]


@subpackage("vte-gtk4")
def _(self):
    self.subdesc = "Gtk4"
    self.depends = [self.parent]
    return [
        "usr/lib/libvte-2.91-gtk4.so.*",
        "usr/lib/girepository-1.0/Vte-3.91.typelib",
    ]


@subpackage("vte-gtk3-devel")
def _(self):
    self.subdesc = "Gtk+3 development files"
    return [
        "usr/include/vte-2.91/vte",
        "usr/lib/libvte-2.91.so",
        "usr/lib/pkgconfig/vte-2.91.pc",
        "usr/share/gir-1.0/Vte-2.91.gir",
        "usr/share/vala/vapi/vte-2.91.*",
    ]


@subpackage("vte-gtk4-devel")
def _(self):
    self.subdesc = "Gtk4 development files"
    return [
        "usr/include/vte-2.91-gtk4/vte",
        "usr/lib/libvte-2.91-gtk4.so",
        "usr/lib/pkgconfig/vte-2.91-gtk4.pc",
        "usr/share/gir-1.0/Vte-3.91.gir",
        "usr/share/vala/vapi/vte-2.91-gtk4.*",
    ]


@subpackage("vte-demos")
def _(self):
    self.subdesc = "example applications"
    self.depends = [self.parent]
    return [
        "usr/bin/vte-2.91",
        "usr/bin/vte-2.91-gtk4",
        "usr/share/applications/org.gnome.Vte.App.Gtk3.desktop",
        "usr/share/xdg-terminals/org.gnome.Vte.App.Gtk3.desktop",
        "usr/share/applications/org.gnome.Vte.App.Gtk4.desktop",
        "usr/share/xdg-terminals/org.gnome.Vte.App.Gtk4.desktop",
    ]
