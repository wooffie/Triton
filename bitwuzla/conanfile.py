from conan import ConanFile
from conan.tools.meson import MesonToolchain, Meson
from conan.tools.gnu import PkgConfigDeps
from conan.tools.scm import Git
from conan.tools.layout import basic_layout


class bitwuzlaConan(ConanFile):
    name = "bitwuzla"
    version = "0.4.0"
    package_type = "library"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/bitwuzla/bitwuzla.git", target=".")
        git.checkout("31330f252ace62954d573e68261acd78c8554db7")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("gmp/6.3.0")

    def generate(self):
        pc = PkgConfigDeps(self)
        pc.generate()
        tc = MesonToolchain(self)
        tc.project_options.pop("wrap_mode")
        tc.generate()

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()

    def package(self):
        meson = Meson(self)
        meson.install()

    def package_info(self):
        self.cpp_info.libs = ["bitwuzla", "bitwuzlals", "bitwuzlabv", "bitwuzlabb"]
        self.cpp_info.set_property("cmake_target_name", "Bitwuzla::bitwuzla")
