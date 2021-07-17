from cbuild.core import paths
from cbuild import cpu

def _make_crossfile(pkg, build_dir):
    if not pkg.build_profile.cross:
        return

    cfpath = pkg.abs_build_wrksrc / build_dir / "cbuild.cross"

    meson_cpu = cpu.match_arch(pkg.build_profile.arch,
        "arm*",     "arm",
        "aarch64*", "aarch64",
        "ppc64*",   "ppc64",
        "ppc*",     "ppc",
        "x86_64*",  "x86_64",
        "i686*",    "x86",
        "riscv64*", "riscv64",
        "*", None
    )

    if not meson_cpu:
        pkg.error(f"unknown architecture: {pkg.build_profile.arch}")

    with open(cfpath, "w") as outf:
        outf.write(f"""
[binaries]
c = '{pkg.tools["CC"]}'
cpp = '{pkg.tools["CXX"]}'
ar = '{pkg.tools["AR"]}'
nm = '{pkg.tools["NM"]}'
ld = '{pkg.tools["LD"]}'
strip = '{pkg.tools["STRIP"]}'
readelf = '{pkg.tools["READELF"]}'
objcopy = '{pkg.tools["OBJCOPY"]}'
pkgconfig = '{pkg.tools["PKG_CONFIG"]}'
llvm-config = '/usr/bin/llvm-config'

[properties]
needs_exe_wrapper = true

[built-in options]
c_args = {str(pkg.get_cflags())}
c_link_args = {str(pkg.get_ldflags())}

cpp_args = {str(pkg.get_cxxflags())}
cpp_link_args = {str(pkg.get_ldflags())}

[host_machine]
system = 'linux'
cpu_family = '{meson_cpu}'
cpu = '{pkg.build_profile.arch}'
endian = '{pkg.build_profile.endian}'
""")

    return cfpath

def configure(pkg, meson_dir = None, build_dir = "build", extra_args = []):
    if not meson_dir:
        meson_dir = "."

    cfp = _make_crossfile(pkg, build_dir)

    cargs = []
    if cfp:
        cargs = ["--cross-file=" + str(
            pkg.chroot_build_wrksrc / cfp.relative_to(pkg.abs_build_wrksrc)
        )]

    pkg.do(
        "meson", [
            "--prefix=/usr",
            "--libdir=/usr/lib",
            "--libexecdir=/usr/libexec",
            "--bindir=/usr/bin",
            "--sbindir=/usr/bin",
            "--includedir=/usr/include",
            "--datadir=/usr/share",
            "--mandir=/usr/share/man",
            "--infodir=/usr/share/info",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--sharedstatedir=/var/lib",
            "--buildtype=plain",
            "--auto-features=auto",
            "--wrap-mode=nodownload",
            "-Ddefault_library=both",
            "-Db_ndebug=true",
            "-Db_staticpic=true"
        ] + cargs + pkg.configure_args + extra_args + [meson_dir, build_dir],
        build = True
    )
