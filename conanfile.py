import os
from conans import ConanFile, CMake, MSBuild, tools

# To add this to the local cache:
# conan export . detours/4.0.1@microsoft/stable

class DetoursConanfile(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    build_requires = "cmake/3.17.3"
    exports_sources = "CMakeLists.txt", "src/*"

    def _configure_cmake(self):
        self.source_folder = os.path.abspath(".")
        self.build_folder = os.path.abspath("bin")
        cmake = CMake(self)

        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs.append("detours")