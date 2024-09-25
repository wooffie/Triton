from conan import ConanFile
from conan.tools.cmake import cmake_layout

class TritonDeps(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("capstone/5.0.1")
        self.requires("bitwuzla/0.4.0")

        self.requires("boost/1.81.0")

    def configure(self):
        self.options["boost"].header_only = True
        
    def layout(self):
        cmake_layout(self)
